from django.db import models

class User(models.Model):
    email = models.CharField(max_length=256)
    fullname = models.CharField(max_length=256)
    encrypted_hashed_pwd = models.CharField(max_length=1024)
    gender = models.CharField(max_length=32)
    mobile_number = models.CharField(max_length=64, null=True)
    active = models.BooleanField(default=True)

class Listing(models.Model):
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=1024)
    gps_coordinates = models.CharField(max_length=128, null=True)
    price_per_night = models.DecimalField(max_digits=15, decimal_places=5)
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ################
    host_user = models.ForeignKey(User, related_name='host_listings', on_delete=models.PROTECT)

class ListingAvailable(models.Model):
    available_date = models.DateField()
    ################
    listing = models.ForeignKey(Listing, related_name='available_dates', on_delete=models.PROTECT)

class StaticAttributes(models.Model):
    attr_type = models.CharField(max_length=128)
    attr_name = models.CharField(max_length=256)
    active = models.BooleanField(default=True)

class ListingAttributes(models.Model):
    listing = models.ForeignKey(Listing, related_name='attributes', on_delete=models.PROTECT)
    attribute = models.ForeignKey(StaticAttributes, related_name='listings', on_delete=models.PROTECT)

class Booking(models.Model):
    name = models.CharField(max_length=256)
    transaction_amount = models.DecimalField(max_digits=15, decimal_places=5)
    canceled_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ################
    listing = models.ForeignKey(Listing, related_name='bookings', on_delete=models.PROTECT)
    guest_user = models.ForeignKey(User, related_name='guest_bookings', on_delete=models.PROTECT)

class BookingDate(models.Model):
    booked_date = models.DateField()
    ################
    booking = models.ForeignKey(Booking, related_name='booked_dates', on_delete=models.PROTECT)

