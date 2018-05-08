import apps.main.models as m
import datetime
import dateutil.parser
import django
import inspect

from django.db import transaction
from django.db.models import Count
from pprint import pprint

def create_static_data():
    if len(m.StaticAttr.objects.all()) == 0:
        m.StaticAttr.objects.create(attr_name='amenities', attr_val='Kitchen')
        m.StaticAttr.objects.create(attr_name='amenities', attr_val='Shampoo')
        m.StaticAttr.objects.create(attr_name='amenities', attr_val='Heating')
        m.StaticAttr.objects.create(attr_name='amenities', attr_val='Air conditioning')
        m.StaticAttr.objects.create(attr_name='amenities', attr_val='Washer')
        m.StaticAttr.objects.create(attr_name='amenities', attr_val='Dryer')
        m.StaticAttr.objects.create(attr_name='amenities', attr_val='Wifi')
        m.StaticAttr.objects.create(attr_name='amenities', attr_val='Breakfast')
        m.StaticAttr.objects.create(attr_name='amenities', attr_val='Indoor fireplace')
        m.StaticAttr.objects.create(attr_name='amenities', attr_val='Buzzer/wireless intercom')
        m.StaticAttr.objects.create(attr_name='amenities', attr_val='Doorman')
        m.StaticAttr.objects.create(attr_name='amenities', attr_val='Hangers')
        m.StaticAttr.objects.create(attr_name='amenities', attr_val='Iron')
        m.StaticAttr.objects.create(attr_name='amenities', attr_val='Hair dryer')
        m.StaticAttr.objects.create(attr_name='amenities', attr_val='Laptop friendly workspace')
        m.StaticAttr.objects.create(attr_name='amenities', attr_val='TV')
        m.StaticAttr.objects.create(attr_name='amenities', attr_val='Crib')
        m.StaticAttr.objects.create(attr_name='amenities', attr_val='High chair')
        m.StaticAttr.objects.create(attr_name='amenities', attr_val='Self check-in')
        m.StaticAttr.objects.create(attr_name='amenities', attr_val='Smoke detector')
        m.StaticAttr.objects.create(attr_name='facilities', attr_val='Free parking on premises')
        m.StaticAttr.objects.create(attr_name='facilities', attr_val='Gym')
        m.StaticAttr.objects.create(attr_name='facilities', attr_val='Hot tub')
        m.StaticAttr.objects.create(attr_name='facilities', attr_val='Pool')
        m.StaticAttr.objects.create(attr_name='stay_type', attr_val='Entire place')
        m.StaticAttr.objects.create(attr_name='stay_type', attr_val='Private room')
        m.StaticAttr.objects.create(attr_name='stay_type', attr_val='Shared room')
        m.StaticAttr.objects.create(attr_name='prop_type', attr_val='House')
        m.StaticAttr.objects.create(attr_name='prop_type', attr_val='Apartment')
        m.StaticAttr.objects.create(attr_name='prop_type', attr_val='Bed and breakfast')
        m.StaticAttr.objects.create(attr_name='prop_type', attr_val='Boutique hotel')
        m.StaticAttr.objects.create(attr_name='prop_type', attr_val='Bungalow')
        m.StaticAttr.objects.create(attr_name='prop_type', attr_val='Cabin')
        m.StaticAttr.objects.create(attr_name='prop_type', attr_val='Chalet')
        m.StaticAttr.objects.create(attr_name='prop_type', attr_val='Cottage')
        m.StaticAttr.objects.create(attr_name='prop_type', attr_val='Guest suite')
        m.StaticAttr.objects.create(attr_name='prop_type', attr_val='Guesthouse')
        m.StaticAttr.objects.create(attr_name='prop_type', attr_val='Hostel')
        m.StaticAttr.objects.create(attr_name='prop_type', attr_val='Hotel')
        m.StaticAttr.objects.create(attr_name='prop_type', attr_val='Loft')
        m.StaticAttr.objects.create(attr_name='prop_type', attr_val='Resort')
        m.StaticAttr.objects.create(attr_name='prop_type', attr_val='Townhouse')
        m.StaticAttr.objects.create(attr_name='prop_type', attr_val='Villa')
        m.StaticAttr.objects.create(attr_name='uniq_type', attr_val='Barn')
        m.StaticAttr.objects.create(attr_name='uniq_type', attr_val='Boat')
        m.StaticAttr.objects.create(attr_name='uniq_type', attr_val='Camper/RV')
        m.StaticAttr.objects.create(attr_name='uniq_type', attr_val='Campsite')
        m.StaticAttr.objects.create(attr_name='uniq_type', attr_val='Casa particular')
        m.StaticAttr.objects.create(attr_name='uniq_type', attr_val='Castle')
        m.StaticAttr.objects.create(attr_name='uniq_type', attr_val='Cave')
        m.StaticAttr.objects.create(attr_name='uniq_type', attr_val='Cycladic house')
        m.StaticAttr.objects.create(attr_name='uniq_type', attr_val='Dammuso')
        m.StaticAttr.objects.create(attr_name='uniq_type', attr_val='Dome house')
        m.StaticAttr.objects.create(attr_name='uniq_type', attr_val='Earth house')
        m.StaticAttr.objects.create(attr_name='uniq_type', attr_val='Farm stay')
        m.StaticAttr.objects.create(attr_name='uniq_type', attr_val='Houseboat')
        m.StaticAttr.objects.create(attr_name='uniq_type', attr_val='Hut')
        m.StaticAttr.objects.create(attr_name='uniq_type', attr_val='Igloo')
        m.StaticAttr.objects.create(attr_name='uniq_type', attr_val='Island')
        m.StaticAttr.objects.create(attr_name='uniq_type', attr_val='Lighthouse')
        m.StaticAttr.objects.create(attr_name='uniq_type', attr_val='Minsu')
        m.StaticAttr.objects.create(attr_name='uniq_type', attr_val='Nature lodge')
        m.StaticAttr.objects.create(attr_name='uniq_type', attr_val='Pension (South Korea)')
        m.StaticAttr.objects.create(attr_name='uniq_type', attr_val='Plane')
        m.StaticAttr.objects.create(attr_name='uniq_type', attr_val='Ryokan')
        m.StaticAttr.objects.create(attr_name='uniq_type', attr_val='Shepherds hut (U.K., France)')
        m.StaticAttr.objects.create(attr_name='uniq_type', attr_val='Tent')
        m.StaticAttr.objects.create(attr_name='uniq_type', attr_val='Tiny house')
        m.StaticAttr.objects.create(attr_name='uniq_type', attr_val='Tipi')
        m.StaticAttr.objects.create(attr_name='uniq_type', attr_val='Train')
        m.StaticAttr.objects.create(attr_name='uniq_type', attr_val='Treehouse')
        m.StaticAttr.objects.create(attr_name='uniq_type', attr_val='Trullo')
        m.StaticAttr.objects.create(attr_name='uniq_type', attr_val='Windmill')
        m.StaticAttr.objects.create(attr_name='uniq_type', attr_val='Yurt')
        m.StaticAttr.objects.create(attr_name='House rules', attr_val='events')
        m.StaticAttr.objects.create(attr_name='House rules', attr_val='pets')
        m.StaticAttr.objects.create(attr_name='House rules', attr_val='smoking')
    return None

def lookup_attr_id(attr_name, attr_val):
    results = m.StaticAttr.objects.filter(attr_name=attr_name).filter(attr_val=attr_val)
    if results and len(results) == 1:
        return results[0].id
    return 0

def ensure_date(val):
    if  type(val) == datetime.date:
        return val
    elif type(val) == datetime:
        return val.date()
    elif type(val) == str:
        return dateutil.parser.parse(val).date()
    return None

def create_user(email, fullname, pwd):
    try:
        return m.User.objects.create(email=email, fullname=fullname, encrypted_hashed_pwd=pwd), None
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

@transaction.atomic
def trans_create_listing(host_user_id, from_date, to_date, name, desc, street_addr, zip_code, country, gps_coordinates, beds, bedrooms, bathrooms, price_per_night, attr_ids):
    from_date = ensure_date(from_date)
    to_date = ensure_date(to_date)
    if  from_date > to_date:
        return None, '{} thru {}: invalid date range!'.format(from_date, to_date)
    listing = m.Listing.objects.create(host_user_id=host_user_id, name=name, desc=desc, street_addr=street_addr, zip_code=zip_code, country=country, gps_coordinates=gps_coordinates, beds=beds, bedrooms=bedrooms, bathrooms=bathrooms, price_per_night=price_per_night)
    for attr_id in attr_ids:
        m.ListingAttr.objects.create(listing_id=listing.id, attr_id=attr_id)
    d = from_date
    delta = datetime.timedelta(days=1)
    while d <= to_date:
        m.BookingState.objects.create(listing_id=listing.id, the_date=d)
        d += delta
    return listing

def create_listing(host_user_id, from_date, to_date, name, desc, street_addr, zip_code, country, gps_coordinates, beds, bedrooms, bathrooms, price_per_night, attr_ids):
    try:
        trans_create_listing(host_user_id, from_date, to_date, name, desc, street_addr, zip_code, country, gps_coordinates, beds, bedrooms, bathrooms, price_per_night, attr_ids)
    except Exception as ex:
        print('{}: {}'.format(type(ex), ex))
    return None

def get_listing(listing_id, context):
    try:
        listing = m.Listing.objects.get(id=listing_id)
        context['listing'] = listing
        context['stay_type'] = listing.attrs.filter(attr__attr_name='stay_type').values_list('attr__attr_val', flat=True)
        context['prop_type'] = listing.attrs.filter(attr__attr_name='prop_type').values_list('attr__attr_val', flat=True)
        context['uniq_type'] = listing.attrs.filter(attr__attr_name='uniq_type').values_list('attr__attr_val', flat=True)
        context['amenities'] = listing.attrs.filter(attr__attr_name='amenities').values_list('attr__attr_val', flat=True)
        context['facilities'] = listing.attrs.filter(attr__attr_name='facilities').values_list('attr__attr_val', flat=True)
        pprint(context)
    except Exception as ex:
        print('{}: {}'.format(type(ex), ex))
        return None

@transaction.atomic
def create_booking(from_date, to_date, name, transaction_amount, listing_id, guest_user_id):
    from_date = ensure_date(from_date)
    to_date = ensure_date(to_date)
    if  from_date > to_date:
        return None, '{} thru {}: invalid date range!'.format(from_date, to_date)
    print('got here')
    booking = m.Booking.objects.create(name=name, transaction_amount=transaction_amount, guest_user_id=guest_user_id)
    m.BookingState.objects.filter(listing_id=listing_id).filter(the_date__gte=from_date).filter(the_date__lte=to_date).update(booking_id=booking.id)
    return booking

@transaction.atomic
def cancel_booking(booking_id):
    booking = m.Booking.objects.get(id=booking_id)
    booking.canceled_at = datetime.datetime.now()
    booking.save()
    m.BookingState.objects.filter(booking_id=booking_id).update(booking_id=None)
    return booking

def get_bookable_listings(from_date, to_date, listing_ids):
    from_date = ensure_date(from_date)
    to_date = ensure_date(to_date)
    if  from_date > to_date:
        return None, '{} thru {}: invalid date range!'.format(from_date, to_date)
    num_days = (to_date - from_date).days + 1
    free_dates = m.BookingState.objects.filter(listing_id__in=listing_ids).filter(the_date__gte=from_date).filter(the_date__lte=to_date).filter(booking_id=None)
    avail_listing_ids = free_dates.values('listing_id').annotate(count=Count('the_date')).filter(count=num_days).values_list('listing_id', flat=True)
    avail_listings = m.Listing.objects.filter(id__in=avail_listing_ids)
    # print(avail_listings.query)
    # print(avail_listings)
    return avail_listings

def get_all_listing_ids():
    return m.Listing.objects.all().values_list('id', flat=True)

def get_all_listings():
    return m.Listing.objects.all()
