import apps.main.models as m
import apps.main.constants as const
import datetime
import dateutil.parser
import django

from django.db import transaction
from django.db.models import Count
from pprint import pprint

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
        context['stay_type'] = const.STAY_TYPE[listing.stay_type]
        context['prop_type'] = const.PROP_TYPE[listing.prop_type]
        context['uniq_type'] = const.UNIQ_TYPE[listing.uniq_type]
        context['amenities'] = const.mask_to_list(const.AMENITIES, listing.amenities_mask)
        context['facilities'] = const.mask_to_list(const.FACILITIES, listing.facilities_mask)
        context['rules'] = const.mask_to_list(const.RULES, listing.rules_mask)
        # pprint(context)
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

def get_bookable_listings_ids(from_date, to_date):
    from_date = ensure_date(from_date)
    to_date = ensure_date(to_date)
    if  from_date > to_date:
        return None, '{} thru {}: invalid date range!'.format(from_date, to_date)
    num_days = (to_date - from_date).days + 1
    try:
        free_dates = m.BookingState.objects.filter(the_date__gte=from_date).filter(the_date__lte=to_date).filter(booking_id=None)
        listing_ids = free_dates.values('listing_id').annotate(count=Count('the_date')).filter(count=num_days).values_list('listing_id', flat=True)
        return listing_ids
    except Exception as ex:
        print('{}: {}'.format(type(ex), ex))
        return None, str(ex)

def get_all_listings():
    try:
        return m.Listing.objects.all()
    except Exception as ex:
        print('{}: {}'.format(type(ex), ex))
        return None, str(ex)
