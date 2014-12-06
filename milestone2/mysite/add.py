import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django
django.setup()

from express.models import *

Diner.objects.all().delete()

diners = [
    Diner(name="Blue Express", loc="LSRC"),
    Diner(name="Twinnie's", loc="CIEMAS"),
    Diner(name="Loop Pizza Grill", loc="Bryan Center"),
    Diner(name="Au Bon Pain", loc="Bryan Center"),
]

for diner in diners:
    diner.save()

import datetime

Item.objects.all().delete()
Type.objects.all().delete()

def NewType(diner_name, type_name):
    return Type(did=Diner.objects.filter(name=diner_name)[0], name=type_name)

types = [
    NewType("Au Bon Pain",      "Sandwiches"),
    NewType("Au Bon Pain",      "Salads"),
    NewType("Loop Pizza Grill", "Salads"),
    NewType("Loop Pizza Grill", "Pastas"),
    NewType("Loop Pizza Grill", "Pizza"),
    NewType("Twinnie's",        "Sandwiches"),
    NewType("Twinnie's",        "Coffees"),
    NewType("Blue Express",     "Sandwiches"),
    NewType("Blue Express",     "Sodas"),
]

for t in types:
    t.save()



def NewItem(type_name, diner_name, item_name, item_price, item_time_to_cook):
    return Item(
        tid=Type.objects.filter(did=Diner.objects.filter(name=diner_name)[0], name=type_name)[0],
        did=Diner.objects.filter(name=diner_name)[0],
        name=item_name,
        price=item_price,
        timeToCook=datetime.datetime.strptime(item_time_to_cook, '%H:%M:%S').time()
    )

items = [
    NewItem("Sandwiches", "Au Bon Pain",      "Turkey Club",           1300, "00:05:00"),
    NewItem("Sandwiches", "Au Bon Pain",      "Two Eggs Sandwiche",    350,  "00:06:00"),
    NewItem("Salads",     "Au Bon Pain",      "Tuna Salad",            1000, "00:04:30"),
    NewItem("Salads",     "Au Bon Pain",      "Classic Chicken Salad", 900,  "00:04:30"),
    
    # NewItem("Sandwiches", "Loop Pizza Grill", "Veggie Sandwiche",      1000, "00:06:00"),
    NewItem("Pastas",     "Loop Pizza Grill", "Bowtie Shrimp Pasta",   1200, "00:10:00"),
    NewItem("Pastas",     "Loop Pizza Grill", "Cajun Chicken Alfredo", 1100, "00:08:00"),
    NewItem("Pizza",      "Loop Pizza Grill", "Five Cheese Pizza",     1600, "00:12:00"),
    NewItem("Pizza",      "Loop Pizza Grill", "Pepperoni Pizza",       1800, "00:15:00"),
    
    NewItem("Sandwiches", "Twinnie's",        "Turkey Club",           1000, "00:06:00"),
    NewItem("Sandwiches", "Twinnie's",        "Tuna Sandwiche",        1200, "00:05:00"),
    NewItem("Coffees",    "Twinnie's",        "Chai Latte",            300,  "00:02:00"),
    NewItem("Coffees",    "Twinnie's",        "Freshly Brew Coffee",   200,  "00:02:00"),

    NewItem("Sandwiches", "Blue Express",     "Turkey Club",           1000, "00:06:00"),
    NewItem("Sandwiches", "Blue Express",     "Beef Cheese Sandwiche", 1100, "00:07:00"),
    NewItem("Sodas",      "Blue Express",     "Coke Cola",             200,  "00:01:00"),
    NewItem("Sodas",      "Blue Express",     "Canada Dry",            200,  "00:01:00"),

]

for i in items:
    i.save()
