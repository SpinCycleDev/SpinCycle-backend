from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from enum import Enum


class StateChoices(Enum):
    AL = 'Alabama',
    AK = 'Alaska',
    AZ = 'Arizona',
    AR = 'Arkansas',
    CA = 'California',
    CO = 'Colorado',
    CT = 'Connecticut',
    DE = 'Delaware',
    FL = 'Florida',
    GA = 'Georgia',
    HI = 'Hawaii',
    ID = 'Idaho',
    IL = 'Illinois',
    IN = 'Indiana',
    IA = 'Iowa',
    KS = 'Kansas',
    KY = 'Kentucky',
    LA = 'Louisiana',
    ME = 'Maine',
    MD = 'Maryland',
    MA = 'Massachusetts',
    MI = 'Michigan',
    MN = 'Minnesota',
    MS = 'Mississippi',
    MO = 'Missouri',
    MT = 'Montana',
    NE = 'Nebraska',
    NV = 'Nevada',
    NH = 'New Hampshire',
    NJ = 'New Jersey',
    NM = 'New Mexico',
    NY = 'New York',
    NC = 'North Carolina',
    ND = 'North Dakota',
    OH = 'Ohio',
    OK = 'Oklahoma',
    OR = 'Oregon',
    PA = 'Pennsylvania',
    RI = 'Rhode Island',
    SC = 'South Carolina',
    SD = 'South Dakota',
    TN = 'Tennessee',
    TX = 'Texas',
    UT = 'Utah',
    VT = 'Vermont',
    VA = 'Virginia',
    WA = 'Washington',
    WV = 'West Virginia',
    WI = 'Wisconsin',
    WY = 'Wyoming',


# Create your models here.

# User Class
class User(models.Model):
    USER_CUSTOMER = 'customer'
    USER_SERVICE_PROVIDER = 'service_provider'
    USER_DRIVER = 'driver'
    USER_TYPE_CHOICES = [
        (USER_CUSTOMER, 'Customer'),
        (USER_SERVICE_PROVIDER, 'Service Provider'),
        (USER_DRIVER, 'Driver'),
    ]
    password = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    user_type = models.CharField(max_length=21, choices=USER_TYPE_CHOICES, default=USER_CUSTOMER)

# Address Class
class Address(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    street_address_line_1 = models.CharField(max_length=100)
    street_address_line_2 = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    # Maybe? vvv
    state = models.CharField(max_length=2, choices=[(state.name, state.value) for state in StateChoices])
    zip_code = models.CharField(max_length=20)
    country = CountryField() 
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

# Driver Class
class Driver(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    vehicle_type = models.CharField(max_length=20)
    license_plate = models.CharField(max_length=20)
    license_number = models.CharField(max_length=20)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    driver_picture = models.ImageField(upload_to='driver_pictures/', default='driver_pictures/default.jpg')

# Customer Class
class Customer(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    laundry_preferences = models.JSONField()
    # order_history = order/model
    