import apps.main.models as m
import datetime
import dateutil.parser
import django
import random

from django.db import transaction
from django.db.models import Count
from pprint import pprint

STATIC_DATA = {
    'amenities': ['Kitchen', 'Shampoo', 'Heating', 'Air conditioning', 'Washer', 'Dryer', 'Wifi', 'Breakfast', 'Indoor fireplace', 'Buzzer/wireless intercom', 'Doorman', 'Hangers', 'Iron', 'Hair dryer', 'Laptop friendly workspace', 'TV', 'Crib', 'High chair', 'Self check-in', 'Smoke detector'],
    'facilities': ['Free parking on premises', 'Gym', 'Hot tub', 'Pool'],
    'prop_type': ['House', 'Apartment','Bed and breakfast','Boutique hotel','Bungalow', 'Cabin','Chalet','Cottage','Guest suite','Guesthouse','Hostel','Hotel','Loft','Resort','Townhouse', 'Villa'],
    'rules': ['events', 'pets', 'smoking'],
    'stay_type': ['Entire place', 'Private room', 'Shared room'],
    'uniq_type': ['Barn','Boat','Camper/RV','Campsite','Casa particular','Castle','Cave','Cycladic house','Dammuso','Dome house','Earth house','Farm stay','Houseboat','Hut','Igloo','Island','Lighthouse','Minsu','Nature lodge','Pension (South Korea)','Plane','Ryokan','Shepherdshut (U.K., France)','Tent','Tiny house','Tipi','Train','Treehouse','Trullo','Windmill','Yurt'],
}

ADDRESSES = [
    { 'street_addr': '5757 Wilshire Blvd #106', 'zip_code': '90036', 'country': 'USA', },
    { 'street_addr': '1161 Westwood Blvd', 'zip_code': '90024', 'country': 'USA', },
    { 'street_addr': '11707 San Vicente Blvd', 'zip_code': '90049', 'country': 'USA', },
    { 'street_addr': '3242 Cahuenga Blvd W', 'zip_code': '90068', 'country': 'USA', },
    { 'street_addr': '5453 Hollywood Blvd', 'zip_code': '90027', 'country': 'USA', },
    { 'street_addr': '138 S Central Ave', 'zip_code': '90012', 'country': 'USA', },
    { 'street_addr': '3722 Crenshaw Blvd', 'zip_code': '90016', 'country': 'USA', },
    { 'street_addr': '8817 S Sepulveda Blvd', 'zip_code': '90045', 'country': 'USA', },
    { 'street_addr': '5855 W Century Blvd', 'zip_code': '90045', 'country': 'USA', },
    { 'street_addr': '120 S Los Angeles St #110', 'zip_code': '90012', 'country': 'USA', },
    { 'street_addr': '555 W 5th St', 'zip_code': '90013', 'country': 'USA', },
    { 'street_addr': '800 W Olympic Blvd #102', 'zip_code': '90015', 'country': 'USA', },
    { 'street_addr': '1850 W Slauson Ave', 'zip_code': '90047', 'country': 'USA', },
    { 'street_addr': '5857 S Central Ave', 'zip_code': '90001', 'country': 'USA', },
    { 'street_addr': '906 Goodrich Blvd', 'zip_code': '90022', 'country': 'USA', },
    { 'street_addr': '7724 Telegraph Rd', 'zip_code': '90040', 'country': 'USA', },
    { 'street_addr': '17254 Lakewood Blvd', 'zip_code': '90706', 'country': 'USA', },
    { 'street_addr': '429 Los Cerritos Center', 'zip_code': '90703', 'country': 'USA', },
    { 'street_addr': '3575 Katella Ave', 'zip_code': '90720', 'country': 'USA', },
    { 'street_addr': '1680 W Lomita Blvd', 'zip_code': '90710', 'country': 'USA', },
    { 'street_addr': '8152 Sunset Blvd', 'zip_code': '90046', 'country': 'USA', },
    { 'street_addr': '5223 W Century Blvd', 'zip_code': '90045', 'country': 'USA', },
    { 'street_addr': '4947 Huntington Dr', 'zip_code': '90032', 'country': 'USA', },
    { 'street_addr': '14742 Oxnard St', 'zip_code': '91411', 'country': 'USA', },
    { 'street_addr': '5933 York Blvd', 'zip_code': '90042', 'country': 'USA', },
    { 'street_addr': '2319 N San Fernando Rd', 'zip_code': '90065', 'country': 'USA', },
    { 'street_addr': '4655 Hollywood Blvd', 'zip_code': '90027', 'country': 'USA', },
    { 'street_addr': '6250 Hollywood Blvd', 'zip_code': '90028', 'country': 'USA', },
    { 'street_addr': '400 World Way', 'zip_code': '90045', 'country': 'USA', },
    { 'street_addr': '11603 Slater St', 'zip_code': '90059', 'country': 'USA', },
    { 'street_addr': '8581 W Pico Blvd', 'zip_code': '90035', 'country': 'USA', },
    { 'street_addr': '189 The Grove Dr', 'zip_code': '90036', 'country': 'USA', },
    { 'street_addr': '901 South La Brea Ave #2', 'zip_code': '90036', 'country': 'USA', },
    { 'street_addr': '4301 W Pico Blvd', 'zip_code': '90019', 'country': 'USA', },
    { 'street_addr': '2575 W Pico Blvd', 'zip_code': '90006', 'country': 'USA', },
    { 'street_addr': '852 S Broadway', 'zip_code': '90014', 'country': 'USA', },
    { 'street_addr': '5601 Melrose Ave', 'zip_code': '90038', 'country': 'USA', },
    { 'street_addr': '1528 North Vermont Avenue C', 'zip_code': '90027', 'country': 'USA', },
    { 'street_addr': '523 N Fairfax Ave', 'zip_code': '90048', 'country': 'USA', },
    { 'street_addr': '10 S De Lacey Ave, Pasadena, CA', 'zip_code': '91105', 'country': 'USA', },
]

NAMES = ['Mansion', 'Party House', 'Riverfront', 'Time of your Life', 'FOMO', 'Boathouse', 'Beach villa', 'Dreams come true', 'Trump Palace', 'Royal Residences', 'Grand Hotel']

def create_static_data():
    if len(m.StaticAttr.objects.all()) == 0:
        for attr_name, attr_list in STATIC_DATA.items():
            for attr_val in attr_list:
                m.StaticAttr.objects.create(attr_name=attr_name, attr_val=attr_val)
    return None

def create_mock_users():
    create_user('jon@email.com', 'Jon L', '$2b$12$wSf0d2tHL8dzQJrMAo7lxODzmVYlKeWMWP961/bNKekhMQoYozgP6')
    create_user('peter@email.com', 'Peter S', '$2b$12$wSf0d2tHL8dzQJrMAo7lxODzmVYlKeWMWP961/bNKekhMQoYozgP6')
    create_user('rick@email.com', 'Rick L', '$2b$12$wSf0d2tHL8dzQJrMAo7lxODzmVYlKeWMWP961/bNKekhMQoYozgP6')
    create_user('fiaz@email.com', 'Fiaz S', '$2b$12$wSf0d2tHL8dzQJrMAo7lxODzmVYlKeWMWP961/bNKekhMQoYozgP6')
    create_user('etienne@email.com', 'Etienne D', '$2b$12$wSf0d2tHL8dzQJrMAo7lxODzmVYlKeWMWP961/bNKekhMQoYozgP6')

def create_mock_listing(addr_idx):
    user_id = random.choice([1, 2, 3, 4, 5])
    name = random.choice(NAMES)
    addr_entry = ADDRESSES[addr_idx]
    from_dt = '2018-{}-{}'.format(random.choice(range(1, 7)), random.choice(range(1, 28)))
    to_dt = '2018-{}-{}'.format(random.choice(range(7, 13)), random.choice(range(1, 28)))
    # fake_geo = '{}{}{}{}'.format(random.choice(from_dt), random.choice(to_dt), random.choice(name), random.choice(name))
    beds = random.choice(range(1, 51))
    rooms = random.choice(range(1, 26))
    baths = random.choice(range(1, 11))
    price = random.choice(range(100, 200))
    other_stuff = []
    other_stuff.append(lookup_attr_id('stay_type', random.choice(STATIC_DATA['stay_type'])))
    other_stuff.append(lookup_attr_id('prop_type', random.choice(STATIC_DATA['prop_type'])))
    other_stuff.append(lookup_attr_id('uniq_type', random.choice(STATIC_DATA['uniq_type'])))
    append_stuff('amenities', other_stuff)
    append_stuff('facilities', other_stuff)
    append_stuff('rules', other_stuff)
    # pprint('{} : {} : {} : {} : {} : {} : {} : {} : {} : {} : {} : {} : {} : {}'.format(user_id, from_dt, to_dt, name, 'description', addr_entry['street_addr'], addr_entry['zip_code'], addr_entry['country'], addr_idx, rooms, beds, baths, price, other_stuff))
    create_listing(user_id, from_dt, to_dt, name, 'description', addr_entry['street_addr'], addr_entry['zip_code'], addr_entry['country'], addr_idx, rooms, beds, baths, price, other_stuff)

def create_mock_listings():
    for i in range(len(ADDRESSES)):
        create_mock_listing(i)

def append_stuff(key, other_stuff):
    for i in range(int(len(STATIC_DATA[key])/2), len(STATIC_DATA[key])):
        choice = lookup_attr_id(key, random.choice(STATIC_DATA[key]))
        if choice not in other_stuff:
            other_stuff.append(choice)

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
