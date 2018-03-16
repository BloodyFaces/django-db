from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from djmoney.models.fields import MoneyField

# Create your models here.
class Airport(models.Model):
    class Meta:
        db_table = 'Airport'
        db_tablespace = 'django_web'
    
    name = models.CharField(max_length=128, null=False, blank=False)
    country = models.CharField(max_length=128, null=False, blank=False)
    city = models.CharField(max_length=128, null=False, blank=False)

    def __str__(self):
        return "%s-%s-%s" % (self.name, self.country, self.city)


class Plane(models.Model):
    class Meta:
        db_table = 'Plane'
        db_tablespace = 'django_web'

    name = models.CharField(max_length=128, null=False, blank=False)
    number_of_sits = models.IntegerField()

class Client(models.Model):
    class Meta:
        db_table = 'Client'
        db_tablespace = 'django_web'

    name = models.CharField(max_length=128, null=False, blank=False)
    surname = models.CharField(max_length=128, null=False, blank=False)
    gender = models.CharField(max_length=10, null=False, blank=False)
    phone_number = PhoneNumberField(blank=False, null=False)
    email = models.EmailField(blank=False, null=False)


class Flight(models.Model):
    class Meta:
        db_table = 'Flight'
        db_tablespace = 'django_web'

    duration = models.DurationField()
    date = models.DateField(auto_now=False, auto_now_add=False)
    departure = models.ForeignKey('Airport', on_delete=models.CASCADE, related_name='%(class)s_departure')
    destination = models.ForeignKey('Airport', on_delete=models.CASCADE, related_name='%(class)s_destination')
    plane = models.ForeignKey('Plane', on_delete=models.CASCADE)

class Ticket(models.Model):
    class Meta:
        db_table = 'Ticket'
        db_tablespace = 'django_web'

    sit_class = models.CharField(max_length=32, null=False, blank=False)
    flight = models.ForeignKey('Flight', on_delete=models.CASCADE)
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    cost = MoneyField(default_currency='EUR', max_digits=10, decimal_places=2)