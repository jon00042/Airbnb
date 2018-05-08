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
    stay_type = models.IntegerField()
    prop_type = models.IntegerField()
    uniq_type = models.IntegerField(null=True)
    beds = models.FloatField()
    bedrooms = models.FloatField()
    bathrooms = models.FloatField()
    price_per_night = models.DecimalField(max_digits=15, decimal_places=5)
    amenities_mask = models.IntegerField()
    facilities_mask = models.IntegerField()
    rules_mask = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ################
    host_user = models.ForeignKey(User, related_name='host_listings', on_delete=models.PROTECT)

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

