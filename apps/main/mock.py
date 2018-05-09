import apps.main.db_layer as db
import apps.main.constants as const
import random

NAMES = ['Mansion', 'Party House', 'Riverfront', 'Time of your Life', 'FOMO', 'YOLO', 'Boathouse', 'Beach villa', 'Dreams come true', 'Trump Palace', 'Royal Residences', 'Grand Hotel']

ADDRESSES = [
    { 'street_addr': '5757 Wilshire Blvd #106', 'postal_code': '90036', 'country': 'USA', },
    { 'street_addr': '1161 Westwood Blvd', 'postal_code': '90024', 'country': 'USA', },
    { 'street_addr': '11707 San Vicente Blvd', 'postal_code': '90049', 'country': 'USA', },
    { 'street_addr': '3242 Cahuenga Blvd W', 'postal_code': '90068', 'country': 'USA', },
    { 'street_addr': '5453 Hollywood Blvd', 'postal_code': '90027', 'country': 'USA', },
    { 'street_addr': '138 S Central Ave', 'postal_code': '90012', 'country': 'USA', },
    { 'street_addr': '3722 Crenshaw Blvd', 'postal_code': '90016', 'country': 'USA', },
    { 'street_addr': '8817 S Sepulveda Blvd', 'postal_code': '90045', 'country': 'USA', },
    { 'street_addr': '5855 W Century Blvd', 'postal_code': '90045', 'country': 'USA', },
    { 'street_addr': '120 S Los Angeles St #110', 'postal_code': '90012', 'country': 'USA', },
    { 'street_addr': '555 W 5th St', 'postal_code': '90013', 'country': 'USA', },
    { 'street_addr': '800 W Olympic Blvd #102', 'postal_code': '90015', 'country': 'USA', },
    { 'street_addr': '1850 W Slauson Ave', 'postal_code': '90047', 'country': 'USA', },
    { 'street_addr': '5857 S Central Ave', 'postal_code': '90001', 'country': 'USA', },
    { 'street_addr': '906 Goodrich Blvd', 'postal_code': '90022', 'country': 'USA', },
    { 'street_addr': '7724 Telegraph Rd', 'postal_code': '90040', 'country': 'USA', },
    { 'street_addr': '17254 Lakewood Blvd', 'postal_code': '90706', 'country': 'USA', },
    { 'street_addr': '429 Los Cerritos Center', 'postal_code': '90703', 'country': 'USA', },
    { 'street_addr': '3575 Katella Ave', 'postal_code': '90720', 'country': 'USA', },
    { 'street_addr': '1680 W Lomita Blvd', 'postal_code': '90710', 'country': 'USA', },
    { 'street_addr': '8152 Sunset Blvd', 'postal_code': '90046', 'country': 'USA', },
    { 'street_addr': '5223 W Century Blvd', 'postal_code': '90045', 'country': 'USA', },
    { 'street_addr': '4947 Huntington Dr', 'postal_code': '90032', 'country': 'USA', },
    { 'street_addr': '14742 Oxnard St', 'postal_code': '91411', 'country': 'USA', },
    { 'street_addr': '5933 York Blvd', 'postal_code': '90042', 'country': 'USA', },
    { 'street_addr': '2319 N San Fernando Rd', 'postal_code': '90065', 'country': 'USA', },
    { 'street_addr': '4655 Hollywood Blvd', 'postal_code': '90027', 'country': 'USA', },
    { 'street_addr': '6250 Hollywood Blvd', 'postal_code': '90028', 'country': 'USA', },
    { 'street_addr': '400 World Way', 'postal_code': '90045', 'country': 'USA', },
    { 'street_addr': '11603 Slater St', 'postal_code': '90059', 'country': 'USA', },
    { 'street_addr': '8581 W Pico Blvd', 'postal_code': '90035', 'country': 'USA', },
    { 'street_addr': '189 The Grove Dr', 'postal_code': '90036', 'country': 'USA', },
    { 'street_addr': '901 South La Brea Ave #2', 'postal_code': '90036', 'country': 'USA', },
    { 'street_addr': '4301 W Pico Blvd', 'postal_code': '90019', 'country': 'USA', },
    { 'street_addr': '2575 W Pico Blvd', 'postal_code': '90006', 'country': 'USA', },
    { 'street_addr': '852 S Broadway', 'postal_code': '90014', 'country': 'USA', },
    { 'street_addr': '5601 Melrose Ave', 'postal_code': '90038', 'country': 'USA', },
    { 'street_addr': '1528 North Vermont Avenue C', 'postal_code': '90027', 'country': 'USA', },
    { 'street_addr': '523 N Fairfax Ave', 'postal_code': '90048', 'country': 'USA', },
]

def create_users():
    db.create_user('jon@email.com', 'Jon L', '$2b$12$wSf0d2tHL8dzQJrMAo7lxODzmVYlKeWMWP961/bNKekhMQoYozgP6')
    db.create_user('peter@email.com', 'Peter S', '$2b$12$wSf0d2tHL8dzQJrMAo7lxODzmVYlKeWMWP961/bNKekhMQoYozgP6')
    db.create_user('rick@email.com', 'Rick L', '$2b$12$wSf0d2tHL8dzQJrMAo7lxODzmVYlKeWMWP961/bNKekhMQoYozgP6')
    db.create_user('fiaz@email.com', 'Fiaz S', '$2b$12$wSf0d2tHL8dzQJrMAo7lxODzmVYlKeWMWP961/bNKekhMQoYozgP6')
    db.create_user('etienne@email.com', 'Etienne D', '$2b$12$wSf0d2tHL8dzQJrMAo7lxODzmVYlKeWMWP961/bNKekhMQoYozgP6')

def create_listing(addr_idx):
    addr_entry = ADDRESSES[addr_idx]
    params_dict = {
        'name': random.choice(NAMES),
        'desc': 'description',
        'street_addr': addr_entry['street_addr'],
        'postal_code': addr_entry['postal_code'],
        'country': addr_entry['country'],
        'gps_coordinates': str(addr_idx),
        'stay_type': random.choice(range(len(const.STAY_TYPE))),
        'prop_type': random.choice(range(len(const.PROP_TYPE))),
        'uniq_type': random.choice(range(len(const.UNIQ_TYPE))),
        'beds': random.choice(range(1, 51)),
        'bedrooms': random.choice(range(1, 26)),
        'bathrooms': random.choice(range(1, 11)),
        'price_per_night': random.choice(range(100, 200)),
        'amenities_mask': random.choice(range(1 << len(const.AMENITIES))),
        'facilities_mask': random.choice(range(1 << len(const.FACILITIES))),
        'rules_mask': random.choice(range(1 << len(const.RULES))),
        'host_user_id': random.choice([1, 2, 3, 4, 5]),
    }
    listing, error = db.create_listing(params_dict)
    if listing:
        from_dt = '2018-{}-{}'.format(random.choice(range(1, 7)), random.choice(range(1, 28)))
        to_dt = '2018-{}-{}'.format(random.choice(range(7, 13)), random.choice(range(1, 28)))
        db.add_listing_dates(listing.id, from_dt, to_dt)

def create_listings():
    for i in range(len(ADDRESSES)):
        create_listing(i)

