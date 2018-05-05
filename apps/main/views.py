import apps.main.db_layer as db

from django.shortcuts import render

def create_data():
    db.create_listing('miami',     '2018-07-28', '2018-08-05')
    db.create_listing('bangkok',   '2018-01-01', '2018-12-31')
    db.create_listing('tokyo',     '2018-06-01', '2018-10-31')
    db.create_listing('singapore', '2018-03-25', '2018-04-26')
    db.create_listing('houston',   '2018-03-01', '2018-08-07')
    db.create_booking('2018-03-24', '2018-03-25', 'bangkok1', 2)
    return None

def index(request):
    # create_data()
    dl = db.get_avail_listings('2018-03-25', '2018-03-30', db.get_all_listing_ids())
    print(dl)
    # create_booking(m.RealBooking, m.RealBookedDate, '2018-06-03', '2018-06-09', listing_id=1)
    return render(request, 'main/index.html')

