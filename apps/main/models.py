from django.db import models

class User(models.Model):
    email = models.CharField(max_length=256, unique=True)
    fullname = models.CharField(max_length=256)
    encrypted_hashed_pwd = models.CharField(max_length=1024)
    gender = models.CharField(max_length=32, null=True)
    mobile_number = models.CharField(max_length=64, null=True)
    active = models.BooleanField(default=True)

class Listing(models.Model):
    name = models.CharField(max_length=256)
    desc = models.TextField(null=True)
    street_addr = models.CharField(max_length=1024)
    zip_code = models.CharField(max_length=64)
    country = models.CharField(max_length=128)
    gps_coordinates = models.CharField(max_length=128, unique=True)
    beds = models.FloatField()
    bedrooms = models.FloatField()
    bathrooms = models.FloatField()
    price_per_night = models.DecimalField(max_digits=15, decimal_places=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ################
    host_user = models.ForeignKey(User, related_name='host_listings', on_delete=models.PROTECT)

class StaticAttr(models.Model):
    attr_type = models.CharField(max_length=128)
    attr_name = models.CharField(max_length=256)
    active = models.BooleanField(default=True)

class ListingAttr(models.Model):
    listing = models.ForeignKey(Listing, related_name='attrs', on_delete=models.PROTECT)
    attr = models.ForeignKey(StaticAttr, related_name='listings', on_delete=models.PROTECT)

class Booking(models.Model):
    name = models.CharField(max_length=256)
    transaction_amount = models.DecimalField(max_digits=15, decimal_places=5)
    canceled_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ################
    guest_user = models.ForeignKey(User, related_name='guest_bookings', on_delete=models.PROTECT)

class BookingState(models.Model):
    the_date = models.DateField()
    booking_id = models.IntegerField(null=True)
    ################
    listing = models.ForeignKey(Listing, related_name='dates', on_delete=models.PROTECT)

