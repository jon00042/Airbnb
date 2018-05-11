import apps.main.db_layer as db
import apps.main.constants as const
import apps.main.keys as keys
import json
import random
import requests

GMAP_GEO_URL_FMT = 'https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'

NAMES = ['Mansion', 'Party House', 'Riverfront', 'Time of your Life', 'FOMO', 'YOLO', 'Boathouse', 'Beach villa', 'Dreams come true', 'Trump Palace', 'Royal Residences', 'Grand Hotel']

ADDRESSES = [
    [ '5757 Wilshire Blvd', '90036', 'USA', ],
    [ '1161 Westwood Blvd', '90024', 'USA', ],
    [ '11707 San Vicente Blvd', '90049', 'USA', ],
    [ '3242 Cahuenga Blvd W', '90068', 'USA', ],
    [ '5453 Hollywood Blvd', '90027', 'USA', ],
    [ '138 S Central Ave', '90012', 'USA', ],
    [ '3722 Crenshaw Blvd', '90016', 'USA', ],
    [ '8817 S Sepulveda Blvd', '90045', 'USA', ],
    [ '5855 W Century Blvd', '90045', 'USA', ],
    [ '120 S Los Angeles St', '90012', 'USA', ],
    [ '555 W 5th St', '90013', 'USA', ],
    [ '800 W Olympic Blvd', '90015', 'USA', ],
    [ '1850 W Slauson Ave', '90047', 'USA', ],
    [ '5857 S Central Ave', '90001', 'USA', ],
    [ '906 Goodrich Blvd', '90022', 'USA', ],
    [ '7724 Telegraph Rd', '90040', 'USA', ],
    [ '17254 Lakewood Blvd', '90706', 'USA', ],
    [ '429 Los Cerritos Center', '90703', 'USA', ],
    [ '3575 Katella Ave', '90720', 'USA', ],
    [ '1680 W Lomita Blvd', '90710', 'USA', ],
    [ '8152 Sunset Blvd', '90046', 'USA', ],
    [ '5223 W Century Blvd', '90045', 'USA', ],
    [ '4947 Huntington Dr', '90032', 'USA', ],
    [ '14742 Oxnard St', '91411', 'USA', ],
    [ '5933 York Blvd', '90042', 'USA', ],
    [ '2319 N San Fernando Rd', '90065', 'USA', ],
    [ '4655 Hollywood Blvd', '90027', 'USA', ],
    [ '6250 Hollywood Blvd', '90028', 'USA', ],
    [ '400 World Way', '90045', 'USA', ],
    [ '11603 Slater St', '90059', 'USA', ],
    [ '8581 W Pico Blvd', '90035', 'USA', ],
    [ '189 The Grove Dr', '90036', 'USA', ],
    [ '901 South La Brea Ave', '90036', 'USA', ],
    [ '4301 W Pico Blvd', '90019', 'USA', ],
    [ '2575 W Pico Blvd', '90006', 'USA', ],
    [ '852 S Broadway', '90014', 'USA', ],
    [ '5601 Melrose Ave', '90038', 'USA', ],
    [ '1528 North Vermont Avenue C', '90027', 'USA', ],
    [ '523 N Fairfax Ave', '90048', 'USA', ],
    [ 'Paseo de la Reforma s/n', '06500', 'Mexico', ],
    [ 'Paseo de la Reforma 476', '06600', 'Mexico', ],
    [ 'Insurgentes Sur 235', '06700', 'Mexico', ],
    [ 'Calle Durango 205 Local 1', '06700', 'Mexico', ],
    [ 'Calle Hamburgo 87', '06600', 'Mexico', ],
    [ '463 Saint-Catherine', 'H3B 1B1', 'Canada', ],
    [ '2050 Rue de Bleury', 'H3A 2J5', 'Canada', ],
    [ '150 Saint-Catherine St', 'H2X 3Y2', 'Canada', ],
    [ '245 Sherbrooke St', 'H2X 1X8', 'Canada', ],
    [ '262 Saint-Catherine St', 'H2X 2A1', 'Canada', ],
]

def create_users():
    db.create_user('jon@email.com', 'Jon L', '$2b$12$wSf0d2tHL8dzQJrMAo7lxODzmVYlKeWMWP961/bNKekhMQoYozgP6')
    db.create_user('peter@email.com', 'Peter S', '$2b$12$wSf0d2tHL8dzQJrMAo7lxODzmVYlKeWMWP961/bNKekhMQoYozgP6')
    db.create_user('rick@email.com', 'Rick L', '$2b$12$wSf0d2tHL8dzQJrMAo7lxODzmVYlKeWMWP961/bNKekhMQoYozgP6')
    db.create_user('fiaz@email.com', 'Fiaz S', '$2b$12$wSf0d2tHL8dzQJrMAo7lxODzmVYlKeWMWP961/bNKekhMQoYozgP6')
    db.create_user('etienne@email.com', 'Etienne D', '$2b$12$wSf0d2tHL8dzQJrMAo7lxODzmVYlKeWMWP961/bNKekhMQoYozgP6')

def create_listing(addr_idx):
    addr_entry = ADDRESSES[addr_idx]
    geo_str = addr_entry[0] + ' ' + addr_entry[1] + ' ' + addr_entry[2]
    geo_str = geo_str.replace(" ", "+")
    geo_url = GMAP_GEO_URL_FMT.format(geo_str, keys.GMAP_API_KEY)
    listing, error = db.get_listing_by_geo_url(geo_url)
    if (listing):
        return None
    response = requests.get(geo_url)
    if response and type(response.text) == str:
        json_dict = json.loads(response.text)
    lat = None
    lng = None
    if json_dict:
        results = json_dict.get('results')
        if type(results) == list and len(results) > 0 and type(results[0]) == dict:
            geometry = results[0].get('geometry')
            if type(geometry) == dict:
                location = geometry.get('location')
                if type(location) == dict:
                    lat = location.get('lat')
                    lng = location.get('lng')
    if not lat or not lng:
        print('failed to parse lat/lng from: {}'.format(response.text))
        return None
    params_dict = {
        'name': random.choice(NAMES),
        'desc': 'description',
        'geo_url': geo_url,
        'geo_json': response.text,
        'geo_coordinates': str(lat) + ':' + str(lng),
        'stay_type': 1 << random.choice(range(len(const.STAY_TYPE))),
        'prop_type': 1 << random.choice(range(len(const.PROP_TYPE))),
        'uniq_type': 1 << random.choice(range(len(const.UNIQ_TYPE))),
        'beds': random.choice(range(1, 51)),
        'bedrooms': random.choice(range(1, 26)),
        'bathrooms': random.choice(range(1, 11)),
        'price_per_night': random.choice(range(100, 200)),
        'amenities_mask': random.choice(range(1 << len(const.AMENITIES))),
        'facilities_mask': random.choice(range(1 << len(const.FACILITIES))),
      # 'rules_mask': random.choice(range(1 << len(const.RULES))),
        'rules_mask': random.choice(range(1 << 3)),
        'host_user_id': random.choice([1, 2, 3, 4, 5]),
    }
    if random.choice(range(10)) == 5:
        params_dict['uniq_type'] = None
    listing, error = db.create_listing(params_dict)
    if listing:
        from_dt = '2018-{}-{}'.format(random.choice(range(1, 7)), random.choice(range(1, 28)))
        to_dt = '2018-{}-{}'.format(random.choice(range(7, 13)), random.choice(range(1, 28)))
        db.add_listing_dates(listing.id, from_dt, to_dt)

def create_listings():
    for i in range(len(ADDRESSES)):
        create_listing(i)

