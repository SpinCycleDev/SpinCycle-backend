from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
    USER_CUSTOMER = 'cutomer'
    USER_SERVICE_PROVIDER = 'service_provider'
    USER_DRIVER = 'driver'
    USER_TYPE_CHOICES = (
        (USER_CUSTOMER, 'Customer'),
        (USER_SERVICE_PROVIDER, 'Service Provider'),
        (USER_DRIVER, 'Driver'),
    )

    user_id = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default=USER_CUSTOMER)