import apps.main.models as m
import datetime
import dateutil.parser

from django.db import transaction
from django.db.models import Count
from pprint import pprint

def ensureDate(val):
    if (type(val) == datetime.date):
        return val
    elif (type(val) == datetime):
        return val.date()
    elif (type(val) == str):
        return dateutil.parser.parse(val).date()
    return None

@transaction.atomic
def create_listing(name, from_date, to_date):
    try:
        from_date = ensureDate(from_date)
        to_date = ensureDate(to_date)
        if (from_date >= to_date):
            return None, '{} thru {}: invalid date range!'.format(from_date, to_date)
        listing = m.Listing.objects.create(name=name)
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
def create_booking(from_date, to_date, name, listing_id):
    try:
        from_date = ensureDate(from_date)
        to_date = ensureDate(to_date)
        if (from_date >= to_date):
            return None, '{} thru {}: invalid date range!'.format(from_date, to_date)
        booking = m.Booking.objects.create(name=name, listing_id=listing_id, canceled=False)
        d = from_date
        delta = datetime.timedelta(days=1)
        while d <= to_date:
            m.BookingDate.objects.create(booking_id=booking.id, booked_date=d)
            d += delta
        return booking
    except Exception as ex:
        print('{}: {}'.format(type(ex), ex))
        return None, ex

def get_avail_listings(from_date, to_date, listing_ids):
    try:
        from_date = ensureDate(from_date)
        to_date = ensureDate(to_date)
        if (from_date >= to_date):
            return None, '{} thru {}: invalid date range!'.format(from_date, to_date)
        num_days = (to_date - from_date).days + 1
        delta = datetime.timedelta(days=1)
        avail_listing_ids = m.ListingAvailable.objects.filter(listing_id__in=listing_ids).filter(available_date__gte=from_date).filter(available_date__lte=to_date).values('listing_id').annotate(count=Count('available_date')).filter(count=num_days).values_list('listing_id', flat=True)
        print(avail_listing_ids.query)
        print(avail_listing_ids)
        booked_listing_ids = m.BookingDate.objects.filter(booked_date__gte=from_date).filter(booked_date__lte=to_date).values_list('booking__listing_id', flat=True).distinct()
        print(booked_listing_ids.query)
        print(booked_listing_ids)
        booked_listing_ids_dict = {}
        for listing_id in booked_listing_ids:
            booked_listing_ids_dict[str(listing_id)] = 1
        results = {}
        for listing_id in avail_listing_ids:
            if str(listing_id) not in booked_listing_ids_dict:
                results[str(listing_id)] = 1
        return results
    except Exception as ex:
        print('{}: {}'.format(type(ex), ex))
        return None, ex

def get_all_listing_ids():
    try:
        return m.Listing.objects.all().values_list('id', flat=True)
    except Exception as ex:
        print('{}: {}'.format(type(ex), ex))
        return None, ex

