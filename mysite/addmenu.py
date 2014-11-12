import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django
from express.models import Type, Diner, Item
django.setup()
import datetime

Item.objects.all().delete()
Type.objects.all().delete()

types = [
    Type(did=Diner.objects.filter(name="Au Bon Pain")[0], name="Sandwiches"),
    Type(did=Diner.objects.filter(name="Au Bon Pain")[0], name="Salads"),
    Type(did=Diner.objects.filter(name="Loop Pizza Grill")[0], name="Salads"),
    Type(did=Diner.objects.filter(name="Loop Pizza Grill")[0], name="Pastas"),
    Type(did=Diner.objects.filter(name="Loop Pizza Grill")[0], name="Pizza"),
    Type(did=Diner.objects.filter(name="Twinnie's")[0], name="Sandwiches"),  
    Type(did=Diner.objects.filter(name="Twinnie's")[0], name="Coffees"),
    Type(did=Diner.objects.filter(name="Blue Express")[0], name="Sandwiches"),
    Type(did=Diner.objects.filter(name="Blue Express")[0], name="Sodas"),
]

for t in types:
    t.save()

items = [
    Item(tid=Type.objects.filter(name="Sandwiches")[0],
         did=Diner.objects.filter(name="Au Bon Pain")[0],
         name="Turkey Club",
         price=1300,
         timeToCook=datetime.datetime.strptime("00:05:00", '%H:%M:%S').time()),
    Item(tid=Type.objects.filter(name="Sandwiches")[0],
         did=Diner.objects.filter(name="Au Bon Pain")[0],
         name="Two Eggs Sandwiche",
         price=350,
         timeToCook=datetime.datetime.strptime("00:06:00", '%H:%M:%S').time()),
    Item(tid=Type.objects.filter(name="Salads")[0],
         did=Diner.objects.filter(name="Au Bon Pain")[0],
         name="Tuna Salad",
         price=1000,
         timeToCook=datetime.datetime.strptime("00:04:30", '%H:%M:%S').time()),
    Item(tid=Type.objects.filter(name="Salads")[0],
         did=Diner.objects.filter(name="Au Bon Pain")[0],
         name="Classic Chicken Salad",
         price=900,
         timeToCook=datetime.datetime.strptime("00:04:30", '%H:%M:%S').time()),
    
    Item(tid=Type.objects.filter(name="Sandwiches")[0],
         did=Diner.objects.filter(name="Loop Pizza Grill")[0],
         name="Veggie Sandwiche",
         price=1000,
         timeToCook=datetime.datetime.strptime("00:06:00", '%H:%M:%S').time()),
    Item(tid=Type.objects.filter(name="Pastas")[0],
         did=Diner.objects.filter(name="Loop Pizza Grill")[0],
         name="Bowtie Shrimp Pasta",
         price=1200,
         timeToCook=datetime.datetime.strptime("00:10:00", '%H:%M:%S').time()),
    Item(tid=Type.objects.filter(name="Pastas")[0],
         did=Diner.objects.filter(name="Loop Pizza Grill")[0],
         name="Cajun Chicken Alfredo",
         price=1100,
         timeToCook=datetime.datetime.strptime("00:08:00", '%H:%M:%S').time()),
    Item(tid=Type.objects.filter(name="Pizza")[0],
         did=Diner.objects.filter(name="Loop Pizza Grill")[0],
         name="Five Cheese Pizza",
         price=1600,
         timeToCook=datetime.datetime.strptime("00:12:00", '%H:%M:%S').time()),
    Item(tid=Type.objects.filter(name="Pizza")[0],
         did=Diner.objects.filter(name="Loop Pizza Grill")[0],
         name="Pepperoni Pizza",
         price=1800,
         timeToCook=datetime.datetime.strptime("00:15:00", '%H:%M:%S').time()),
    Item(tid=Type.objects.filter(name="Sandwiches")[0],
         did=Diner.objects.filter(name="Twinnie's")[0],
         name="Turkey Club",
         price=1000,
         timeToCook=datetime.datetime.strptime("00:06:00", '%H:%M:%S').time()),
    Item(tid=Type.objects.filter(name="Sandwiches")[0],
         did=Diner.objects.filter(name="Twinnie's")[0],
         name="Tuna Sandwiche",
         price=1200,
         timeToCook=datetime.datetime.strptime("00:05:00", '%H:%M:%S').time()),
    Item(tid=Type.objects.filter(name="Coffees")[0],
         did=Diner.objects.filter(name="Twinnie's")[0],
         name="Chai Latte",
         price=300,
         timeToCook=datetime.datetime.strptime("00:02:00", '%H:%M:%S').time()),
    Item(tid=Type.objects.filter(name="Coffees")[0],
         did=Diner.objects.filter(name="Twinnie's")[0],
         name="Freshly Brew Coffee",
         price=200,
         timeToCook=datetime.datetime.strptime("00:02:00", '%H:%M:%S').time()),
    Item(tid=Type.objects.filter(name="Sandwiches")[0],
         did=Diner.objects.filter(name="Blue Express")[0],
         name="Turkey Club",
         price=1000,
         timeToCook=datetime.datetime.strptime("00:06:00", '%H:%M:%S').time()),
    Item(tid=Type.objects.filter(name="Sandwiches")[0],
         did=Diner.objects.filter(name="Blue Express")[0],
         name="Beef Cheese Sandwiche",
         price=1100,
         timeToCook=datetime.datetime.strptime("00:07:00", '%H:%M:%S').time()),
    Item(tid=Type.objects.filter(name="Sodas")[0],
         did=Diner.objects.filter(name="Blue Express")[0],
         name="Coke Cola",
         price=200,
         timeToCook=datetime.datetime.strptime("00:01:00", '%H:%M:%S').time()),
    Item(tid=Type.objects.filter(name="Sodas")[0],
         did=Diner.objects.filter(name="Blue Express")[0],
         name="Canada Dry",
         price=200,
         timeToCook=datetime.datetime.strptime("00:01:00", '%H:%M:%S').time()),
]



for i in items:
    i.save()
