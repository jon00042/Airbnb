from django.db import models

class Listing(models.Model):
    name = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ListingAvailable(models.Model):
    available_date = models.DateField()
    ################
    listing = models.ForeignKey(Listing, related_name='available_dates', on_delete=models.PROTECT)

class Booking(models.Model):
    name = models.CharField(max_length=256)
    canceled = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ################
    listing = models.ForeignKey(Listing, related_name='bookings', on_delete=models.PROTECT)

class BookingDate(models.Model):
    booked_date = models.DateField()
    ################
    booking = models.ForeignKey(Booking, related_name='booked_dates', on_delete=models.PROTECT)

