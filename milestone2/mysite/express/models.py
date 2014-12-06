from django.db import models

# Create your models here.
class Diner(models.Model):
    did = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    loc = models.CharField(max_length=200)

class Type(models.Model):
    did = models.ForeignKey('Diner')
    tid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

class Item(models.Model):
    iid = models.AutoField(primary_key=True)
    tid = models.ForeignKey('Type')
    did = models.ForeignKey('Diner')
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    timeToCook = models.TimeField()

class User(models.Model):
    cardid = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=30)
    email = models.EmailField()

class Order(models.Model):
    oid = models.AutoField(primary_key=True)
    cardid = models.ForeignKey('User')
    did = models.ForeignKey('Diner')
    timePlaced = models.DateTimeField()
    scheduledPickUpTime = models.DateTimeField()
    PENDING = 'PE'
    ACCEPTED = 'AC'
    READY = 'RE'
    PICKED = 'PI'
    STAT_CHOICES = (
        (PENDING, 'Pending'),
        (ACCEPTED, 'Accepted'),
        (READY, 'Ready'),
        (PICKED, 'Picked'),
    )
    stat = models.CharField(
        max_length=2,
        choices=STAT_CHOICES,
        default=PENDING    
    )

class Include(models.Model):
    oid = models.ForeignKey('Order')
    iid = models.ForeignKey('Item')

class DinerHour(models.Model):
    did = models.ForeignKey('Diner')
    MONDAY = 'MO'
    TUESDAY = 'TU'
    WEDNESDAY = 'WE'
    THURSDAY = 'TH'
    FRIDAY = 'FR'
    SATURDAY = 'SA'
    SUNDAY = 'SU'
    DAY_CHOICES = (
        (MONDAY, 'Monday'),
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THURSDAY, 'Thursday'),
        (FRIDAY, 'Friday'),
        (SATURDAY, 'Saturday'),
        (SUNDAY, 'Sunday'),
    )
    day = models.CharField(
        max_length=2,
        choices=DAY_CHOICES,
    )
    openTime = models.TimeField()
    closeTime = models.TimeField()

class ItemHour(models.Model):
    iid = models.ForeignKey('Item')
    MONDAY = 'MO'
    TUESDAY = 'TU'
    WEDNESDAY = 'WE'
    THURSDAY = 'TH'
    FRIDAY = 'FR'
    SATURDAY = 'SA'
    SUNDAY = 'SU'
    DAY_CHOICES = (
        (MONDAY, 'Monday'),
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THURSDAY, 'Thursday'),
        (FRIDAY, 'Friday'),
        (SATURDAY, 'Saturday'),
        (SUNDAY, 'Sunday'),
    )
    day = models.CharField(
        max_length=2,
        choices=DAY_CHOICES,
    )
    openTime = models.TimeField()
    closeTime = models.TimeField()
