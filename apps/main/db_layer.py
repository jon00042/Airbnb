import apps.main.models as m
import datetime
import dateutil.parser
import django
import inspect

from django.db import transaction
from django.db.models import Count

def create_static_data():
    if len(m.StaticAttr.objects.all()) == 0:
        m.StaticAttr.objects.create(attr_type='Amenities', attr_name='Kitchen')
        m.StaticAttr.objects.create(attr_type='Amenities', attr_name='Shampoo')
        m.StaticAttr.objects.create(attr_type='Amenities', attr_name='Heating')
        m.StaticAttr.objects.create(attr_type='Amenities', attr_name='Air conditioning')
        m.StaticAttr.objects.create(attr_type='Amenities', attr_name='Washer')
        m.StaticAttr.objects.create(attr_type='Amenities', attr_name='Dryer')
        m.StaticAttr.objects.create(attr_type='Amenities', attr_name='Wifi')
        m.StaticAttr.objects.create(attr_type='Amenities', attr_name='Breakfast')
        m.StaticAttr.objects.create(attr_type='Amenities', attr_name='Indoor fireplace')
        m.StaticAttr.objects.create(attr_type='Amenities', attr_name='Buzzer/wireless intercom')
        m.StaticAttr.objects.create(attr_type='Amenities', attr_name='Doorman')
        m.StaticAttr.objects.create(attr_type='Amenities', attr_name='Hangers')
        m.StaticAttr.objects.create(attr_type='Amenities', attr_name='Iron')
        m.StaticAttr.objects.create(attr_type='Amenities', attr_name='Hair dryer')
        m.StaticAttr.objects.create(attr_type='Amenities', attr_name='Laptop friendly workspace')
        m.StaticAttr.objects.create(attr_type='Amenities', attr_name='TV')
        m.StaticAttr.objects.create(attr_type='Amenities', attr_name='Crib')
        m.StaticAttr.objects.create(attr_type='Amenities', attr_name='High chair')
        m.StaticAttr.objects.create(attr_type='Amenities', attr_name='Self check-in')
        m.StaticAttr.objects.create(attr_type='Amenities', attr_name='Smoke detector')
        m.StaticAttr.objects.create(attr_type='Facilities', attr_name='Free parking on premises')
        m.StaticAttr.objects.create(attr_type='Facilities', attr_name='Gym')
        m.StaticAttr.objects.create(attr_type='Facilities', attr_name='Hot tub')
        m.StaticAttr.objects.create(attr_type='Facilities', attr_name='Pool')
        m.StaticAttr.objects.create(attr_type='Home type', attr_name='Entire place')
        m.StaticAttr.objects.create(attr_type='Home type', attr_name='Private room')
        m.StaticAttr.objects.create(attr_type='Home type', attr_name='Shared room')
        m.StaticAttr.objects.create(attr_type='Property type', attr_name='House')
        m.StaticAttr.objects.create(attr_type='Property type', attr_name='Apartment')
        m.StaticAttr.objects.create(attr_type='Property type', attr_name='Bed and breakfast')
        m.StaticAttr.objects.create(attr_type='Property type', attr_name='Boutique hotel')
        m.StaticAttr.objects.create(attr_type='Property type', attr_name='Bungalow')
        m.StaticAttr.objects.create(attr_type='Property type', attr_name='Cabin')
        m.StaticAttr.objects.create(attr_type='Property type', attr_name='Chalet')
        m.StaticAttr.objects.create(attr_type='Property type', attr_name='Cottage')
        m.StaticAttr.objects.create(attr_type='Property type', attr_name='Guest suite')
        m.StaticAttr.objects.create(attr_type='Property type', attr_name='Guesthouse')
        m.StaticAttr.objects.create(attr_type='Property type', attr_name='Hostel')
        m.StaticAttr.objects.create(attr_type='Property type', attr_name='Hotel')
        m.StaticAttr.objects.create(attr_type='Property type', attr_name='Loft')
        m.StaticAttr.objects.create(attr_type='Property type', attr_name='Resort')
        m.StaticAttr.objects.create(attr_type='Property type', attr_name='Townhouse')
        m.StaticAttr.objects.create(attr_type='Property type', attr_name='Villa')
        m.StaticAttr.objects.create(attr_type='Unique homes', attr_name='Barn')
        m.StaticAttr.objects.create(attr_type='Unique homes', attr_name='Boat')
        m.StaticAttr.objects.create(attr_type='Unique homes', attr_name='Camper/RV')
        m.StaticAttr.objects.create(attr_type='Unique homes', attr_name='Campsite')
        m.StaticAttr.objects.create(attr_type='Unique homes', attr_name='Casa particular')
        m.StaticAttr.objects.create(attr_type='Unique homes', attr_name='Castle')
        m.StaticAttr.objects.create(attr_type='Unique homes', attr_name='Cave')
        m.StaticAttr.objects.create(attr_type='Unique homes', attr_name='Cycladic house')
        m.StaticAttr.objects.create(attr_type='Unique homes', attr_name='Dammuso')
        m.StaticAttr.objects.create(attr_type='Unique homes', attr_name='Dome house')
        m.StaticAttr.objects.create(attr_type='Unique homes', attr_name='Earth house')
        m.StaticAttr.objects.create(attr_type='Unique homes', attr_name='Farm stay')
        m.StaticAttr.objects.create(attr_type='Unique homes', attr_name='Houseboat')
        m.StaticAttr.objects.create(attr_type='Unique homes', attr_name='Hut')
        m.StaticAttr.objects.create(attr_type='Unique homes', attr_name='Igloo')
        m.StaticAttr.objects.create(attr_type='Unique homes', attr_name='Island')
        m.StaticAttr.objects.create(attr_type='Unique homes', attr_name='Lighthouse')
        m.StaticAttr.objects.create(attr_type='Unique homes', attr_name='Minsu')
        m.StaticAttr.objects.create(attr_type='Unique homes', attr_name='Nature lodge')
        m.StaticAttr.objects.create(attr_type='Unique homes', attr_name='Pension (South Korea)')
        m.StaticAttr.objects.create(attr_type='Unique homes', attr_name='Plane')
        m.StaticAttr.objects.create(attr_type='Unique homes', attr_name='Ryokan')
        m.StaticAttr.objects.create(attr_type='Unique homes', attr_name='Shepherds hut (U.K., France)')
        m.StaticAttr.objects.create(attr_type='Unique homes', attr_name='Tent')
        m.StaticAttr.objects.create(attr_type='Unique homes', attr_name='Tiny house')
        m.StaticAttr.objects.create(attr_type='Unique homes', attr_name='Tipi')
        m.StaticAttr.objects.create(attr_type='Unique homes', attr_name='Train')
        m.StaticAttr.objects.create(attr_type='Unique homes', attr_name='Treehouse')
        m.StaticAttr.objects.create(attr_type='Unique homes', attr_name='Trullo')
        m.StaticAttr.objects.create(attr_type='Unique homes', attr_name='Windmill')
        m.StaticAttr.objects.create(attr_type='Unique homes', attr_name='Yurt')
        m.StaticAttr.objects.create(attr_type='House rules', attr_name='events')
        m.StaticAttr.objects.create(attr_type='House rules', attr_name='pets')
        m.StaticAttr.objects.create(attr_type='House rules', attr_name='smoking')
    return None

def lookup_attr_id(attr_type, attr_name):
    results = m.StaticAttr.objects.filter(attr_type=attr_type).filter(attr_name=attr_name)
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
