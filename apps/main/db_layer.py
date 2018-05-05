import apps.main.models as m
import datetime
import dateutil.parser

from django.db import transaction
from django.db.models import Count, Q

def create_static_data():
    if len(m.StaticAttributes.objects.all()) == 0:
        m.StaticAttributes.objects.create(attr_type='Amenities', attr_name='Kitchen')
        m.StaticAttributes.objects.create(attr_type='Amenities', attr_name='Shampoo')
        m.StaticAttributes.objects.create(attr_type='Amenities', attr_name='Heating')
        m.StaticAttributes.objects.create(attr_type='Amenities', attr_name='Air conditioning')
        m.StaticAttributes.objects.create(attr_type='Amenities', attr_name='Washer')
        m.StaticAttributes.objects.create(attr_type='Amenities', attr_name='Dryer')
        m.StaticAttributes.objects.create(attr_type='Amenities', attr_name='Wifi')
        m.StaticAttributes.objects.create(attr_type='Amenities', attr_name='Breakfast')
        m.StaticAttributes.objects.create(attr_type='Amenities', attr_name='Indoor fireplace')
        m.StaticAttributes.objects.create(attr_type='Amenities', attr_name='Buzzer/wireless intercom')
        m.StaticAttributes.objects.create(attr_type='Amenities', attr_name='Doorman')
        m.StaticAttributes.objects.create(attr_type='Amenities', attr_name='Hangers')
        m.StaticAttributes.objects.create(attr_type='Amenities', attr_name='Iron')
        m.StaticAttributes.objects.create(attr_type='Amenities', attr_name='Hair dryer')
        m.StaticAttributes.objects.create(attr_type='Amenities', attr_name='Laptop friendly workspace')
        m.StaticAttributes.objects.create(attr_type='Amenities', attr_name='TV')
        m.StaticAttributes.objects.create(attr_type='Amenities', attr_name='Crib')
        m.StaticAttributes.objects.create(attr_type='Amenities', attr_name='High chair')
        m.StaticAttributes.objects.create(attr_type='Amenities', attr_name='Self check-in')
        m.StaticAttributes.objects.create(attr_type='Amenities', attr_name='Smoke detector')
        m.StaticAttributes.objects.create(attr_type='Facilities', attr_name='Free parking on premises')
        m.StaticAttributes.objects.create(attr_type='Facilities', attr_name='Gym')
        m.StaticAttributes.objects.create(attr_type='Facilities', attr_name='Hot tub')
        m.StaticAttributes.objects.create(attr_type='Facilities', attr_name='Pool')
        m.StaticAttributes.objects.create(attr_type='Property type', attr_name='House')
        m.StaticAttributes.objects.create(attr_type='Property type', attr_name='Apartment')
        m.StaticAttributes.objects.create(attr_type='Property type', attr_name='Bed and breakfast')
        m.StaticAttributes.objects.create(attr_type='Property type', attr_name='Boutique hotel')
        m.StaticAttributes.objects.create(attr_type='Property type', attr_name='Bungalow')
        m.StaticAttributes.objects.create(attr_type='Property type', attr_name='Cabin')
        m.StaticAttributes.objects.create(attr_type='Property type', attr_name='Chalet')
        m.StaticAttributes.objects.create(attr_type='Property type', attr_name='Cottage')
        m.StaticAttributes.objects.create(attr_type='Property type', attr_name='Guest suite')
        m.StaticAttributes.objects.create(attr_type='Property type', attr_name='Guesthouse')
        m.StaticAttributes.objects.create(attr_type='Property type', attr_name='Hostel')
        m.StaticAttributes.objects.create(attr_type='Property type', attr_name='Hotel')
        m.StaticAttributes.objects.create(attr_type='Property type', attr_name='Loft')
        m.StaticAttributes.objects.create(attr_type='Property type', attr_name='Resort')
        m.StaticAttributes.objects.create(attr_type='Property type', attr_name='Townhouse')
        m.StaticAttributes.objects.create(attr_type='Property type', attr_name='Villa')
        m.StaticAttributes.objects.create(attr_type='Unique homes', attr_name='Barn')
        m.StaticAttributes.objects.create(attr_type='Unique homes', attr_name='Boat')
        m.StaticAttributes.objects.create(attr_type='Unique homes', attr_name='Camper/RV')
        m.StaticAttributes.objects.create(attr_type='Unique homes', attr_name='Campsite')
        m.StaticAttributes.objects.create(attr_type='Unique homes', attr_name='Casa particular')
        m.StaticAttributes.objects.create(attr_type='Unique homes', attr_name='Castle')
        m.StaticAttributes.objects.create(attr_type='Unique homes', attr_name='Cave')
        m.StaticAttributes.objects.create(attr_type='Unique homes', attr_name='Cycladic house')
        m.StaticAttributes.objects.create(attr_type='Unique homes', attr_name='Dammuso')
        m.StaticAttributes.objects.create(attr_type='Unique homes', attr_name='Dome house')
        m.StaticAttributes.objects.create(attr_type='Unique homes', attr_name='Earth house')
        m.StaticAttributes.objects.create(attr_type='Unique homes', attr_name='Farm stay')
        m.StaticAttributes.objects.create(attr_type='Unique homes', attr_name='Houseboat')
        m.StaticAttributes.objects.create(attr_type='Unique homes', attr_name='Hut')
        m.StaticAttributes.objects.create(attr_type='Unique homes', attr_name='Igloo')
        m.StaticAttributes.objects.create(attr_type='Unique homes', attr_name='Island')
        m.StaticAttributes.objects.create(attr_type='Unique homes', attr_name='Lighthouse')
        m.StaticAttributes.objects.create(attr_type='Unique homes', attr_name='Minsu')
        m.StaticAttributes.objects.create(attr_type='Unique homes', attr_name='Nature lodge')
        m.StaticAttributes.objects.create(attr_type='Unique homes', attr_name='Pension (South Korea)')
        m.StaticAttributes.objects.create(attr_type='Unique homes', attr_name='Plane')
        m.StaticAttributes.objects.create(attr_type='Unique homes', attr_name='Ryokan')
        m.StaticAttributes.objects.create(attr_type='Unique homes', attr_name='Shepherds hut (U.K., France)')
        m.StaticAttributes.objects.create(attr_type='Unique homes', attr_name='Tent')
        m.StaticAttributes.objects.create(attr_type='Unique homes', attr_name='Tiny house')
        m.StaticAttributes.objects.create(attr_type='Unique homes', attr_name='Tipi')
        m.StaticAttributes.objects.create(attr_type='Unique homes', attr_name='Train')
        m.StaticAttributes.objects.create(attr_type='Unique homes', attr_name='Treehouse')
        m.StaticAttributes.objects.create(attr_type='Unique homes', attr_name='Trullo')
        m.StaticAttributes.objects.create(attr_type='Unique homes', attr_name='Windmill')
        m.StaticAttributes.objects.create(attr_type='Unique homes', attr_name='Yurt')
        m.StaticAttributes.objects.create(attr_type='House rules', attr_name='Suitable for events')
        m.StaticAttributes.objects.create(attr_type='House rules', attr_name='Pets allowed')
        m.StaticAttributes.objects.create(attr_type='House rules', attr_name='Smoking allowed')
    return None

def ensureDate(val):
    if (type(val) == datetime.date):
        return val
    elif (type(val) == datetime):
        return val.date()
    elif (type(val) == str):
        return dateutil.parser.parse(val).date()
    return None

def create_user(email, fullname, pwd, gender):
    try:
        return m.User.objects.create(email=email, fullname=fullname, encrypted_hashed_pwd=pwd, gender=gender)
    except Exception as ex:
        print('{}: {}'.format(type(ex), ex))
        return None, ex

@transaction.atomic
def create_listing(from_date, to_date, name, address, gps_coordinates, price_per_night, beds, bedrooms, bathrooms, host_user_id, static_attrs):
    try:
        from_date = ensureDate(from_date)
        to_date = ensureDate(to_date)
        if (from_date >= to_date):
            return None, '{} thru {}: invalid date range!'.format(from_date, to_date)
        listing = m.Listing.objects.create(name=name, address=address, gps_coordinates=gps_coordinates, price_per_night=price_per_night, beds=beds, bedrooms=bedrooms, bathrooms=bathrooms, host_user_id=host_user_id)
        for static_attr in static_attrs:
            attr_type, attr_name = static_attr
            attribute = m.StaticAttributes.objects.get(Q(attr_type=attr_type) & Q(attr_name=attr_name))
            m.ListingAttributes.objects.create(listing_id=listing.id, attribute_id=attribute.id)
        d = from_date
        delta = datetime.timedelta(days=1)
        while d <= to_date:
            m.ListingAvailable.objects.create(listing_id = listing.id, available_date=d)
            d += delta
        return listing
    except Exception as ex:
        print('{}: {}'.format(type(ex), ex))
        return None, ex

@transaction.atomic
def create_booking(from_date, to_date, name, transaction_amount, listing_id, guest_user_id):
    try:
        from_date = ensureDate(from_date)
        to_date = ensureDate(to_date)
        if (from_date >= to_date):
            return None, '{} thru {}: invalid date range!'.format(from_date, to_date)
        booking = m.Booking.objects.create(name=name, transaction_amount=transaction_amount, listing_id=listing_id, guest_user_id=guest_user_id)
        d = from_date
        delta = datetime.timedelta(days=1)
        while d <= to_date:
            m.BookingDate.objects.create(booking_id=booking.id, booked_date=d)
            d += delta
        return booking
    except Exception as ex:
        print('{}: {}'.format(type(ex), ex))
        return None, ex

def get_bookable_listings(from_date, to_date, listing_ids):
    try:
        from_date = ensureDate(from_date)
        to_date = ensureDate(to_date)
        if (from_date >= to_date):
            return None, '{} thru {}: invalid date range!'.format(from_date, to_date)
        num_days = (to_date - from_date).days + 1
        booked_listing_ids = m.BookingDate.objects.filter(booking__listing_id__in=listing_ids).filter(booked_date__gte=from_date).filter(booked_date__lte=to_date).values_list('booking__listing_id', flat=True).distinct()
        # print(booked_listing_ids.query)
        # print(booked_listing_ids)
        bookable_listing_ids = m.ListingAvailable.objects.filter(listing_id__in=listing_ids).exclude(listing_id__in=booked_listing_ids).filter(available_date__gte=from_date).filter(available_date__lte=to_date).values('listing_id').annotate(count=Count('available_date')).filter(count=num_days).values_list('listing_id', flat=True)
        # print(bookable_listing_ids.query)
        # print(bookable_listing_ids)
        bookable_listing_ids_dict = {}
        for bookable_listing_id in bookable_listing_ids:
            bookable_listing_ids_dict[str(bookable_listing_id)] = 1
        return bookable_listing_ids_dict
    except Exception as ex:
        print('{}: {}'.format(type(ex), ex))
        return None, ex

def get_all_listing_ids():
    try:
        return m.Listing.objects.all().values_list('id', flat=True)
    except Exception as ex:
        print('{}: {}'.format(type(ex), ex))
        return None, ex

