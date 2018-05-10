import apps.main.constants as const
import apps.main.models as m
import datetime
import dateutil.parser
import django
import json

from django.db import transaction
from django.db.models import Count

def ensure_date(val):
    if  type(val) == datetime.date:
        return val
    elif type(val) == datetime:
        return val.date()
    elif type(val) == str:
        return dateutil.parser.parse(val).date()
    return None

def create_user(email, fullname, encrypted_hashed_pwd):
    try:
        return m.User.objects.create(email=email, fullname=fullname, encrypted_hashed_pwd=encrypted_hashed_pwd), None
    except django.db.utils.IntegrityError:
        return None, 'email already in use!'
    except Exception as ex:
        print('{}: {}'.format(type(ex), ex))
        return None, str(ex)

def get_user(email):
    try:
        return m.User.objects.get(email=email), None
    except m.User.DoesNotExist:
        return None, 'Login attempt failed!'
    except Exception as ex:
        print('{}: {}'.format(type(ex), ex))
        return None, str(ex)

def create_listing(params_dict):
    try:
        return m.Listing.objects.create(**params_dict), None
    except Exception as ex:
        print('{}: {}'.format(type(ex), ex))
        return None, str(ex)

@transaction.atomic
def add_listing_dates_trans(listing_id, from_date, to_date):
    from_date = ensure_date(from_date)
    to_date = ensure_date(to_date)
    if  from_date > to_date:
        raise Exception('{} thru {}: invalid date range!'.format(from_date, to_date))
    d = from_date
    delta = datetime.timedelta(days=1)
    while d <= to_date:
        m.BookingState.objects.create(listing_id=listing_id, the_date=d)
        d += delta

def add_listing_dates(listing_id, from_date, to_date):
    try:
        add_listing_dates_trans(listing_id, from_date, to_date)
    except Exception as ex:
        print('{}: {}'.format(type(ex), ex))

def get_listing(listing_id, context):
    try:
        listing = m.Listing.objects.get(id=listing_id)
        context['listing'] = listing
    except Exception as ex:
        print('{}: {}'.format(type(ex), ex))

@transaction.atomic
def create_booking_trans(from_date, to_date, name, transaction_amount, listing_id, guest_user_id):
    from_date = ensure_date(from_date)
    to_date = ensure_date(to_date)
    if  from_date > to_date:
        raise Exception('{} thru {}: invalid date range!'.format(from_date, to_date))
    booking = m.Booking.objects.create(name=name, transaction_amount=transaction_amount, guest_user_id=guest_user_id)
    m.BookingState.objects.filter(listing_id=listing_id).filter(the_date__gte=from_date).filter(the_date__lte=to_date).update(booking_id=booking.id)
    return booking

@transaction.atomic
def cancel_booking_trans(booking_id):
    booking = m.Booking.objects.get(id=booking_id)
    booking.canceled_at = datetime.datetime.now()
    booking.save()
    m.BookingState.objects.filter(booking_id=booking_id).update(booking_id=None)
    return booking

def get_all_listings():
    try:
        return m.Listing.objects.all()
    except Exception as ex:
        print('{}: {}'.format(type(ex), ex))
        return None, str(ex)

def get_bookable_listings(from_date, to_date):
    if from_date or to_date:  # sic: wan't to raise an error
        try:
            from_date = ensure_date(from_date)
            to_date = ensure_date(to_date)
            if  from_date > to_date:
                raise Exception('{} thru {}: invalid date range!'.format(from_date, to_date))
            num_days = (to_date - from_date).days + 1
            listing_ids = m.BookingState.objects.filter(the_date__gte=from_date).filter(the_date__lte=to_date).filter(booking_id=None).values('listing_id').distinct()
            return m.Listing.objects.filter(id__in=listing_ids)
        except Exception as ex:
            print('{}: {}'.format(type(ex), ex))
    try:
        return m.Listing.objects.all()
    except Exception as ex:
        print('{}: {}'.format(type(ex), ex))

def get_filtered_listing_ids_dict(criteria_dict):
    from_date = criteria_dict.get('from_date')
    to_date = criteria_dict.get('to_date')
    listings = get_bookable_listings(from_date, to_date)
    stay_type_mask = const.list_to_mask(const.STAY_TYPE, criteria_dict.get('stay_type'))
    prop_type_mask = const.list_to_mask(const.PROP_TYPE, criteria_dict.get('prop_type'))
    amenities_mask = const.list_to_mask(const.AMENITIES, criteria_dict.get('amenities'))
    facilities_mask = const.list_to_mask(const.FACILITIES, criteria_dict.get('facilities'))
    uniq_type_mask = const.list_to_mask(const.UNIQ_TYPE, criteria_dict.get('uniq_type'))
    filtered_listing_ids_dict = {}
    for listing in listings:
        if stay_type_mask and not listing.stay_type & stay_type_mask:
            continue
        if amenities_mask and listing.amenities_mask & amenities_mask != amenities_mask:
            continue
        if facilities_mask and listing.facilities_mask & facilities_mask != facilities_mask:
            continue
        if prop_type_mask and not listing.prop_type & prop_type_mask:
            continue
        if uniq_type_mask and not listing.uniq_type & uniq_type_mask:
            continue
        filtered_listing_ids_dict[listing.id] = 1
    return filtered_listing_ids_dict

