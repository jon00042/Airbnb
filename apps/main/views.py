import apps.main.db_layer as db

from django.shortcuts import render
from pprint import pprint

def create_mock_data():
    db.create_static_data()
    db.create_user('jon@email.com', 'Jon L', 'xxx', 'M')
    db.create_user('peter@email.com', 'Peter S', 'xxx', 'M')
    db.create_listing('2018-07-28', '2018-08-05', 'miami', 'addr', None, 100, 1, 1, 1, 1, [])
    db.create_listing('2018-01-01', '2018-12-31', 'bangkok', 'addr', None, 100, 1, 1, 1, 1, [])
    db.create_listing('2018-06-01', '2018-10-31', 'tokyo', 'addr', None, 100, 1, 1, 1, 1, [])
    db.create_listing('2018-03-25', '2018-04-26', 'singapore', 'addr', None, 100, 1, 1, 1, 1, [])
    db.create_listing('2018-03-01', '2018-08-07', 'houston', 'addr', None, 100, 1, 1, 1, 1, [])
    db.create_booking('2018-03-24', '2018-03-25', 'bangkok1', 1000, 2, 2)
    return None

def index(request):
    # create_mock_data()
    # l = db.get_bookable_listings('2018-03-25', '2018-03-30', db.get_all_listing_ids())
    # pprint(l)
    return render(request, 'main/index.html')

