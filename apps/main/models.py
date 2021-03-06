import apps.main.constants as const
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
    geo_url = models.CharField(max_length=1024, unique=True)
    geo_json = models.TextField()
    geo_coordinates = models.CharField(max_length=128, unique=True)
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
    ################
    @property
    def geo_lat(self):
        return self.geo_coordinates.split(':')[0]
    ################
    @property
    def geo_lng(self):
        return self.geo_coordinates.split(':')[1]
    ################
    @property
    def price_per_night_str(self):
        if self.price_per_night + 1 - self.price_per_night == 1:
            return '${:.0f}'.format(self.price_per_night)
        return '${:.2f}'.format(self.price_per_night)
    ################
    @property
    def beds_str(self):
        if self.beds == 1:
            return '1 bed'
        if self.beds + 1 - self.beds == 1:
            return '{:.0f} beds'.format(self.beds)
        return '{:.2f} beds'.format(self.beds)
    ################
    @property
    def bedrooms_str(self):
        if self.bedrooms == 1:
            return '1 bedroom'
        if self.bedrooms + 1 - self.bedrooms == 1:
            return '{:.0f} bedrooms'.format(self.bedrooms)
        return '{:.2f} bedrooms'.format(self.bedrooms)
    ################
    @property
    def bathrooms_str(self):
        if self.bathrooms == 1:
            return '1 bathroom'
        if self.bathrooms + 1 - self.bathrooms == 1:
            return '{:.0f} bathrooms'.format(self.bathrooms)
        return '{:.2f} bathrooms'.format(self.bathrooms)
    ################
    @property
    def stay_type_str(self):
        arr = const.mask_to_list(const.STAY_TYPE, self.stay_type)
        if not arr or len(arr) < 1:
            return ''
        return arr[0]
    ################
    @property
    def prop_type_str(self):
        arr = const.mask_to_list(const.PROP_TYPE, self.prop_type)
        if not arr or len(arr) < 1:
            return ''
        return arr[0]
    ################
    @property
    def uniq_type_str(self):
        arr = const.mask_to_list(const.UNIQ_TYPE, self.uniq_type)
        if not arr or len(arr) < 1:
            return ''
        return arr[0]
    ################
    @property
    def amenities_list(self):
        return const.mask_to_list(const.AMENITIES, self.amenities_mask)
    ################
    @property
    def facilities_list(self):
        return const.mask_to_list(const.FACILITIES, self.facilities_mask)
    ################
    # @property
    # def rules_list(self):
    #     print(const.RULES)
    #     return const.mask_to_list(const.RULES, self.rules_mask)

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

