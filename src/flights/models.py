from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from djmoney.models.fields import MoneyField

# Create your models here.
class Airport(models.Model):
    class Meta:
        db_table = 'Airport'
    
    name = models.CharField(max_length=128, null=False, blank=False)
    country = models.CharField(max_length=128, null=False, blank=False)
    city = models.CharField(max_length=128, null=False, blank=False)

    def __str__(self):
        return "%s" % (self.name)


class Plane(models.Model):
    class Meta:
        db_table = 'Plane'

    name = models.CharField(max_length=128, null=False, blank=False)
    number_of_sits = models.IntegerField()

    def __str__(self):
        return "%s" % (self.name)

class Client(models.Model):
    class Meta:
        db_table = 'Client'

    name = models.CharField(max_length=128, null=False, blank=False)
    surname = models.CharField(max_length=128, null=False, blank=False)
    gender = models.CharField(max_length=10, null=False, blank=False)
    phone_number = PhoneNumberField(blank=False, null=False)
    email = models.EmailField(blank=False, null=False)

    def __str__(self):
        return "%s %s" % (self.name, self.surname)


class Flight(models.Model):
    class Meta:
        db_table = 'Flight'

    duration = models.DurationField()
    date = models.DateField(auto_now=False, auto_now_add=False)
    departure = models.ForeignKey('Airport', on_delete=models.CASCADE, related_name='%(class)s_departure')
    destination = models.ForeignKey('Airport', on_delete=models.CASCADE, related_name='%(class)s_destination')
    plane = models.ForeignKey('Plane', on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % (self.id)

class Ticket(models.Model):
    class Meta:
        db_table = 'Ticket'

    sit_class = models.CharField(max_length=32, null=False, blank=False)
    flight = models.ForeignKey('Flight', on_delete=models.CASCADE)
    client = models.ForeignKey('Client', on_delete=models.CASCADE, null=True)
    cost = MoneyField(default_currency='EUR', max_digits=10, decimal_places=2)

    def __str__(self):
        return "%s" % (self.id)

