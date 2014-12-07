import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django
django.setup()

from express.models import *

# Diners
# ------
Diner.objects.all().delete()

diners = [
    Diner(name="Blue Express", loc="LSRC"),
    Diner(name="Twinnie's", loc="CIEMAS"),
    Diner(name="Loop Pizza Grill", loc="Bryan Center"),
    Diner(name="Au Bon Pain", loc="Bryan Center"),
]

for diner in diners:
    diner.save()

from datetime import datetime

Item.objects.all().delete()
Type.objects.all().delete()

# Types
# -----

def NewType(diner_name, type_name):
    return Type(did=Diner.objects.filter(name=diner_name)[0], name=type_name)

types = [
    NewType("Au Bon Pain",      "Sandwiches"),
    NewType("Au Bon Pain",      "Salads"),
    NewType("Au Bon Pain",      "Wraps"),    
    NewType("Loop Pizza Grill", "Sandwiches"),
    NewType("Loop Pizza Grill", "Salads"),
    NewType("Loop Pizza Grill", "Pizza Pies"),   
    NewType("Twinnie's",        "Breakfast"),
    NewType("Twinnie's",        "Sandwiches"),
    NewType("Twinnie's",        "Coffees"),
    NewType("Blue Express",     "Sandwiches"),
    NewType("Blue Express",     "Sodas"),
]

for t in types:
    t.save()


# Items
# -----

def NewItem(type_name, diner_name, item_name, item_price, item_time_to_cook):
    return Item(
        tid=Type.objects.filter(did=Diner.objects.filter(name=diner_name)[0], name=type_name)[0],
        did=Diner.objects.filter(name=diner_name)[0],
        name=item_name,
        price=item_price,
        timeToCook=datetime.strptime(item_time_to_cook, '%H:%M:%S').time()
    )

items = [
    NewItem("Sandwiches", "Au Bon Pain",      "Turkey Club",           800, "00:05:00"),
    NewItem("Sandwiches", "Au Bon Pain",      "Two Eggs Sandwiche",    350,  "00:03:30"),
    NewItem("Sandwiches", "Au Bon Pain",      "The Veggie",            550,  "00:04:00"),
    NewItem("Sandwiches", "Au Bon Pain",      "Grilled Chicken",       650,  "00:10:00"),
    NewItem("Sandwiches", "Au Bon Pain",      "Caprese",               550,  "00:04:00"),
    NewItem("Sandwiches", "Au Bon Pain",      "Salmon Wasabi",         900,  "00:11:00"),
    NewItem("Sandwiches", "Au Bon Pain",      "Chipotle Black Bean",   750,  "00:08:00"),
    NewItem("Sandwiches", "Au Bon Pain",      "Cranberry Brie",        650,  "00:05:00"),
    NewItem("Sandwiches", "Au Bon Pain",      "Mediterranean",         550,  "00:05:00"),
    
    NewItem("Salads",     "Au Bon Pain",      "Tuna Salad",            1000, "00:05:30"),
    NewItem("Salads",     "Au Bon Pain",      "Classic Chicken Salad", 900,  "00:04:30"),
    NewItem("Salads",     "Au Bon Pain",      "Turkey & Swiss",        850, "00:08:30"),
    NewItem("Salads",     "Au Bon Pain",      "Ham & Cheddar",         900,  "00:06:00"),
    NewItem("Salads",     "Au Bon Pain",      "Thai Peanut Chicken",   950,  "00:07:30"),
    NewItem("Salads",     "Au Bon Pain",      "Vegetarian Deluxe",     700,  "00:05:00"),
    NewItem("Salads",     "Au Bon Pain",      "Chicken with Avocado",  800,  "00:08:00"),
    NewItem("Salads",     "Au Bon Pain",      "Turkey Apple Brie",     850,  "00:09:00"),
    NewItem("Salads",     "Au Bon Pain",      "Southwest Chicken",     850,  "00:08:30"),
    
    NewItem("Wraps",      "Au Bon Pain",      "Southwest Chicken",     850,  "00:08:30"),
    NewItem("Wraps",      "Au Bon Pain",      "Chicken Caesar",        950,  "00:07:00"),
    NewItem("Wraps",      "Au Bon Pain",      "The Veggie",            850,  "00:08:30"),
    NewItem("Wraps",      "Au Bon Pain",      "Napa Chicken",          650,  "00:06:30"),
    NewItem("Wraps",      "Au Bon Pain",      "Turkey Wrap",           600,  "00:06:00"),
    NewItem("Wraps",      "Au Bon Pain",      "Tuna Wrap",             1000,  "00:09:00"),
    
    # NewItem("Sandwiches", "Loop Pizza Grill", "Veggie Sandwiche",      1000, "00:06:00"),
    NewItem("Sandwiches", "Loop Pizza Grill", "Loop Burber",           699, "00:14:00"),
    NewItem("Sandwiches", "Loop Pizza Grill", "Cheese Burber",         759, "00:15:00"),
    NewItem("Sandwiches", "Loop Pizza Grill", "Bacon Cheddar",         869, "00:16:00"),
    NewItem("Sandwiches", "Loop Pizza Grill", "Mushroom Swiss",        869, "00:13:00"),
    NewItem("Sandwiches", "Loop Pizza Grill", "BBQ Bacon Cheddar",     879, "00:17:00"),
    NewItem("Sandwiches", "Loop Pizza Grill", "Bacon Cheddar",         869, "00:16:00"),
    NewItem("Sandwiches", "Loop Pizza Grill", "Cajun & Jack Cheese",   789, "00:13:30"),
    NewItem("Sandwiches", "Loop Pizza Grill", "Black Bean Burger",     799, "00:10:00"),
    NewItem("Sandwiches", "Loop Pizza Grill", "Veggie Melt Ciabatta",  799, "00:09:00"),
    NewItem("Sandwiches", "Loop Pizza Grill", "Grilled Portabello",    859, "00:13:00"), 
    
    NewItem("Salads",     "Loop Pizza Grill", "Asian Chicken",         799, "00:08:00"),
    NewItem("Salads",     "Loop Pizza Grill", "Crunchy Broccoli",      779, "00:06:30"),
    NewItem("Salads",     "Loop Pizza Grill", "Goat Cheese",           779, "00:07:30"),
    NewItem("Salads",     "Loop Pizza Grill", "Caesar Chicken",        799, "00:06:30"),
    NewItem("Salads",     "Loop Pizza Grill", "Garden with Chicken",   769, "00:09:30"),
    NewItem("Salads",     "Loop Pizza Grill", "Mediterranean",         779, "00:07:30"),
    NewItem("Salads",     "Loop Pizza Grill", "Crispy Chicken",        829, "00:08:30"),
    
    NewItem("Pizza Pies", "Loop Pizza Grill", "Five Cheese Pizza",     1429, "00:12:00"),
    NewItem("Pizza Pies", "Loop Pizza Grill", "Pepperoni Pizza",       1429, "00:15:00"),
    NewItem("Pizza Pies", "Loop Pizza Grill", "Meat Market",           1429, "00:13:00"),
    NewItem("Pizza Pies", "Loop Pizza Grill", "Farmers Market",        1429, "00:12:00"),
    
    NewItem("Sandwiches", "Twinnie's",        "Turkey Club",           650, "00:06:30"),
    NewItem("Sandwiches", "Twinnie's",        "Chicken Pita",          525, "00:05:00"),
    NewItem("Sandwiches", "Twinnie's",        "Panini",                650, "00:07:00"),
    NewItem("Sandwiches", "Twinnie's",        "Peanut Tuna",           625, "00:06:00"),
    NewItem("Sandwiches", "Twinnie's",        "Roast Beef",            675, "00:08:30"),
    NewItem("Sandwiches", "Twinnie's",        "Reuben",                625, "00:05:00"),
    NewItem("Sandwiches", "Twinnie's",        "Turkey Muffaletta",     650, "00:07:30"),
    NewItem("Sandwiches", "Twinnie's",        "Twinnie's Cuban",       675, "00:04:30"),
    
    NewItem("Breakfast",  "Twinnie's",        "Assorted Muffins",       195, "00:02:30"),
    NewItem("Breakfast",  "Twinnie's",        "Scones",                 225, "00:02:00"),
    NewItem("Breakfast",  "Twinnie's",        "Assorted Bagels",        175, "00:03:30"),
    NewItem("Breakfast",  "Twinnie's",        "Cinnamon Rolls",         85, "00:02:00"),  
    NewItem("Breakfast",  "Twinnie's",        "Filled Croissants",      275, "00:04:00"),
    NewItem("Breakfast",  "Twinnie's",        "Plain Croissants",       225, "00:03:30"),
    NewItem("Breakfast",  "Twinnie's",        "Fruit Salad",            350, "00:04:30"),
    
    NewItem("Coffees",    "Twinnie's",        "Chai Latte",            365,  "00:02:00"),
    NewItem("Coffees",    "Twinnie's",        "Freshly Brew Coffee",   225,  "00:02:00"),
    NewItem("Coffees",    "Twinnie's",        "Tazo Hot Tea",          215,  "00:02:00"),
    NewItem("Coffees",    "Twinnie's",        "Americano",             275,  "00:03:00"),
    NewItem("Coffees",    "Twinnie's",        "Cappuccino",            355,  "00:03:00"),
    NewItem("Coffees",    "Twinnie's",        "Caramel Macchiato",     425,  "00:03:30"),
    NewItem("Coffees",    "Twinnie's",        "Latte",                 355,  "00:03:00"),
    NewItem("Coffees",    "Twinnie's",        "White Chocolate Mocha", 415,  "00:03:30"),

    NewItem("Sandwiches", "Blue Express",     "Turkey Club",           800, "00:06:00"),
    NewItem("Sandwiches", "Blue Express",     "Beef Cheese Sandwiche", 1100, "00:07:00"),
    NewItem("Sandwiches", "Blue Express",     "Caribbean Jerk Chicken", 575, "00:08:00"),
    NewItem("Sandwiches", "Blue Express",     "BBQ Chicken",            700,  "00:07:30"),
    NewItem("Sandwiches", "Blue Express",     "Philly Steak",           1175, "00:10:00"),
    NewItem("Sandwiches", "Blue Express",     "Portobello Mushroom",    850,  "00:08:30"),
    NewItem("Sandwiches", "Blue Express",     "Ckicken Shawarma",       850,  "00:07:30"),
    NewItem("Sandwiches", "Blue Express",     "Gyro",                   650,  "00:05:30"),
    
    NewItem("Sodas",      "Blue Express",     "Coke Cola",             200,  "00:01:00"),
    NewItem("Sodas",      "Blue Express",     "Canada Dry",            200,  "00:01:00"),
    NewItem("Sodas",      "Blue Express",     "Fanta Orange",          200,  "00:01:00"),
    NewItem("Sodas",      "Blue Express",     "Sprite",                200,  "00:01:00"),
    NewItem("Sodas",      "Blue Express",     "Dr. Pepper",            200,  "00:01:00"),
    NewItem("Sodas",      "Blue Express",     "Mountain Dew",          200,  "00:01:00"),
]

for i in items:
    i.save()

# Users
# -----
User.objects.all().delete()

users = [
    User(123456789, 'Somebody', '9191234567', 'somebody@something.com')
]

for u in users:
    u.save()

# Orders
# ------
Order.objects.all().delete()

orders = [
    Order(
        cardid=User.objects.get(cardid='123456789'),
        did=Diner.objects.get(name="Blue Express"),
        timePlaced=datetime.now(),
        scheduledPickUpTime=datetime.now(),
        # stat='PE',
    )
]

for o in orders:
    o.save()


# DinerHours
# ----------
DinerHour.objects.all().delete()

def NewDinerHour(diner_name, day, openTime, closeTime):
    return DinerHour(
        did=Diner.objects.filter(name=diner_name)[0],
        day=day,
        openTime=datetime.strptime(openTime, '%H:%M:%S').time(),
        closeTime=datetime.strptime(closeTime, '%H:%M:%S').time(),
    )

diner_hours = [
    NewDinerHour("Au Bon Pain", "MO", "07:00:00", "12:00:00"),
    NewDinerHour("Au Bon Pain", "SA", "07:00:00", "12:00:00"),
]

for d in diner_hours:
    d.save()

# ItemHours
# ---------

def NewItemHour(diner_name, item_name, day, openTime, closeTime):
    return ItemHour(
        iid=Item.objects.filter(did=Diner.objects.filter(name=diner_name)[0], name=item_name)[0],
        day=day,
        openTime=datetime.strptime(openTime, '%H:%M:%S').time(),
        closeTime=datetime.strptime(closeTime, '%H:%M:%S').time(),
    )

item_hours = [
    NewItemHour("Au Bon Pain", "Turkey Club", "MO", "07:00:00", "12:00:00"),
    NewItemHour("Au Bon Pain", "Turkey Club", "SA", "07:00:00", "12:00:00"),
]

for i in item_hours:
    i.save()