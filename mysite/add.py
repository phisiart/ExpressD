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
    
    NewItem("Wraps",      "Au Bon Pain",      "Chicken Caesar",        950,  "00:07:00"),
    NewItem("Wraps",      "Au Bon Pain",      "The Veggie Wrap",       850,  "00:08:30"),
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
    NewDinerHour("Au Bon Pain", "MO", "07:00:00", "24:00:00"),
    NewDinerHour("Au Bon Pain", "TU", "07:00:00", "24:00:00"),
    NewDinerHour("Au Bon Pain", "WE", "07:00:00", "24:00:00"),
    NewDinerHour("Au Bon Pain", "TH", "07:00:00", "24:00:00"),
    NewDinerHour("Au Bon Pain", "FR", "07:00:00", "24:00:00"),
    NewDinerHour("Au Bon Pain", "SA", "07:00:00", "22:00:00"),
    NewDinerHour("Au Bon Pain", "SU", "07:00:00", "22:00:00"),
    
    NewDinerHour("Loop Pizza Grill", "MO", "10:00:00", "22:00:00"),
    NewDinerHour("Loop Pizza Grill", "TU", "10:00:00", "22:00:00"),
    NewDinerHour("Loop Pizza Grill", "WE", "10:00:00", "22:00:00"),
    NewDinerHour("Loop Pizza Grill", "TH", "10:00:00", "22:00:00"),
    NewDinerHour("Loop Pizza Grill", "FR", "10:00:00", "22:00:00"),
    NewDinerHour("Loop Pizza Grill", "SA", "11:00:00", "21:00:00"),
    NewDinerHour("Loop Pizza Grill", "SU", "11:00:00", "21:00:00"),
    
    NewDinerHour("Twinnie's", "MO", "08:00:00", "21:00:00"),
    NewDinerHour("Twinnie's", "TU", "08:00:00", "21:00:00"),
    NewDinerHour("Twinnie's", "WE", "08:00:00", "21:00:00"),
    NewDinerHour("Twinnie's", "TH", "08:00:00", "21:00:00"),
    NewDinerHour("Twinnie's", "FR", "08:00:00", "21:00:00"),
    NewDinerHour("Twinnie's", "SA", "11:00:00", "19:00:00"),
    NewDinerHour("Twinnie's", "SU", "11:00:00", "19:00:00"),
    
    NewDinerHour("Blue Express", "MO", "10:00:00", "22:00:00"),
    NewDinerHour("Blue Express", "TU", "10:00:00", "22:00:00"),
    NewDinerHour("Blue Express", "WE", "10:00:00", "22:00:00"),
    NewDinerHour("Blue Express", "TH", "10:00:00", "22:00:00"),
    NewDinerHour("Blue Express", "FR", "10:00:00", "22:00:00"),
    NewDinerHour("Blue Express", "SA", "11:00:00", "22:00:00"),
    NewDinerHour("Blue Express", "SU", "11:00:00", "22:00:00"),
    
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
    NewItemHour("Au Bon Pain", "Turkey Club", "MO", "12:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Turkey Club", "TU", "12:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Turkey Club", "WE", "12:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Turkey Club", "TH", "12:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Turkey Club", "FR", "12:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Turkey Club", "SA", "14:00:00", "22:00:00"),
    NewItemHour("Au Bon Pain", "Turkey Club", "SU", "14:00:00", "22:00:00"),
    
    NewItemHour("Au Bon Pain", "Two Eggs Sandwiche", "MO", "07:00:00", "12:00:00"),
    NewItemHour("Au Bon Pain", "Two Eggs Sandwiche", "TU", "07:00:00", "12:00:00"),
    NewItemHour("Au Bon Pain", "Two Eggs Sandwiche", "WE", "07:00:00", "12:00:00"),
    NewItemHour("Au Bon Pain", "Two Eggs Sandwiche", "TH", "07:00:00", "12:00:00"),
    NewItemHour("Au Bon Pain", "Two Eggs Sandwiche", "FR", "07:00:00", "12:00:00"),
    NewItemHour("Au Bon Pain", "Two Eggs Sandwiche", "SA", "07:00:00", "12:00:00"),
    NewItemHour("Au Bon Pain", "Two Eggs Sandwiche", "SU", "07:00:00", "12:00:00"),
    
    NewItemHour("Au Bon Pain", "The Veggie", "MO", "12:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "The Veggie", "TU", "12:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "The Veggie", "WE", "12:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "The Veggie", "TH", "12:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "The Veggie", "FR", "12:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "The Veggie", "SA", "14:00:00", "22:00:00"),
    NewItemHour("Au Bon Pain", "The Veggie", "SU", "14:00:00", "22:00:00"),
    
    NewItemHour("Au Bon Pain", "Grilled Chicken", "MO", "12:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Grilled Chicken", "TU", "12:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Grilled Chicken", "WE", "12:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Grilled Chicken", "TH", "12:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Grilled Chicken", "FR", "12:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Grilled Chicken", "SA", "14:00:00", "22:00:00"),
    NewItemHour("Au Bon Pain", "Grilled Chicken", "SU", "14:00:00", "22:00:00"),
    
    NewItemHour("Au Bon Pain", "Caprese", "MO", "12:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Caprese", "TU", "12:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Caprese", "WE", "12:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Caprese", "TH", "12:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Caprese", "FR", "12:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Caprese", "SA", "14:00:00", "22:00:00"),
    NewItemHour("Au Bon Pain", "Caprese", "SU", "14:00:00", "22:00:00"),
    
    NewItemHour("Au Bon Pain", "Salmon Wasabi", "MO", "12:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Salmon Wasabi", "TU", "12:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Salmon Wasabi", "WE", "12:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Salmon Wasabi", "TH", "12:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Salmon Wasabi", "FR", "12:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Salmon Wasabi", "SA", "14:00:00", "22:00:00"),
    NewItemHour("Au Bon Pain", "Salmon Wasabi", "SU", "14:00:00", "22:00:00"),
    
    NewItemHour("Au Bon Pain", "Chipotle Black Bean", "MO", "12:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Chipotle Black Bean", "TU", "12:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Chipotle Black Bean", "WE", "12:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Chipotle Black Bean", "TH", "12:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Chipotle Black Bean", "FR", "12:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Chipotle Black Bean", "SA", "14:00:00", "22:00:00"),
    NewItemHour("Au Bon Pain", "Chipotle Black Bean", "SU", "14:00:00", "22:00:00"),
    
    NewItemHour("Au Bon Pain", "Cranberry Brie", "MO", "12:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Cranberry Brie", "TU", "12:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Cranberry Brie", "WE", "12:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Cranberry Brie", "TH", "12:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Cranberry Brie", "FR", "12:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Cranberry Brie", "SA", "14:00:00", "22:00:00"),
    NewItemHour("Au Bon Pain", "Cranberry Brie", "SU", "14:00:00", "22:00:00"),
    
    NewItemHour("Au Bon Pain", "Mediterranean", "MO", "12:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Mediterranean", "TU", "12:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Mediterranean", "WE", "12:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Mediterranean", "TH", "12:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Mediterranean", "FR", "12:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Mediterranean", "SA", "14:00:00", "22:00:00"),
    NewItemHour("Au Bon Pain", "Mediterranean", "SU", "14:00:00", "22:00:00"),
    
    NewItemHour("Au Bon Pain", "Tuna Salad", "MO", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Tuna Salad", "TU", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Tuna Salad", "WE", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Tuna Salad", "TH", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Tuna Salad", "FR", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Tuna Salad", "SA", "07:00:00", "22:00:00"),
    NewItemHour("Au Bon Pain", "Tuna Salad", "SU", "07:00:00", "22:00:00"),
    
    NewItemHour("Au Bon Pain", "Classic Chicken Salad", "MO", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Classic Chicken Salad", "TU", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Classic Chicken Salad", "WE", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Classic Chicken Salad", "TH", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Classic Chicken Salad", "FR", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Classic Chicken Salad", "SA", "07:00:00", "22:00:00"),
    NewItemHour("Au Bon Pain", "Classic Chicken Salad", "SU", "07:00:00", "22:00:00"),
    
    NewItemHour("Au Bon Pain", "Turkey & Swiss", "MO", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Turkey & Swiss", "TU", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Turkey & Swiss", "WE", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Turkey & Swiss", "TH", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Turkey & Swiss", "FR", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Turkey & Swiss", "SA", "07:00:00", "22:00:00"),
    NewItemHour("Au Bon Pain", "Turkey & Swiss", "SU", "07:00:00", "22:00:00"),
    
    NewItemHour("Au Bon Pain", "Ham & Cheddar", "MO", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Ham & Cheddar", "TU", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Ham & Cheddar", "WE", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Ham & Cheddar", "TH", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Ham & Cheddar", "FR", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Ham & Cheddar", "SA", "07:00:00", "22:00:00"),
    NewItemHour("Au Bon Pain", "Ham & Cheddar", "SU", "07:00:00", "22:00:00"),
    
    NewItemHour("Au Bon Pain", "Thai Peanut Chicken", "MO", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Thai Peanut Chicken", "TU", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Thai Peanut Chicken", "WE", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Thai Peanut Chicken", "TH", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Thai Peanut Chicken", "FR", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Thai Peanut Chicken", "SA", "07:00:00", "22:00:00"),
    NewItemHour("Au Bon Pain", "Thai Peanut Chicken", "SU", "07:00:00", "22:00:00"),
    
    NewItemHour("Au Bon Pain", "Vegetarian Deluxe", "MO", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Vegetarian Deluxe", "TU", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Vegetarian Deluxe", "WE", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Vegetarian Deluxe", "TH", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Vegetarian Deluxe", "FR", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Vegetarian Deluxe", "SA", "07:00:00", "22:00:00"),
    NewItemHour("Au Bon Pain", "Vegetarian Deluxe", "SU", "07:00:00", "22:00:00"),
    
    NewItemHour("Au Bon Pain", "Chicken with Avocado", "MO", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Chicken with Avocado", "TU", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Chicken with Avocado", "WE", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Chicken with Avocado", "TH", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Chicken with Avocado", "FR", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Chicken with Avocado", "SA", "07:00:00", "22:00:00"),
    NewItemHour("Au Bon Pain", "Chicken with Avocado", "SU", "07:00:00", "22:00:00"),
    
    NewItemHour("Au Bon Pain", "Vegetarian Deluxe", "MO", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Vegetarian Deluxe", "TU", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Vegetarian Deluxe", "WE", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Vegetarian Deluxe", "TH", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Vegetarian Deluxe", "FR", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Vegetarian Deluxe", "SA", "07:00:00", "22:00:00"),
    NewItemHour("Au Bon Pain", "Vegetarian Deluxe", "SU", "07:00:00", "22:00:00"),
    
    NewItemHour("Au Bon Pain", "Turkey Apple Brie", "MO", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Turkey Apple Brie", "TU", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Turkey Apple Brie", "WE", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Turkey Apple Brie", "TH", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Turkey Apple Brie", "FR", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Turkey Apple Brie", "SA", "07:00:00", "22:00:00"),
    NewItemHour("Au Bon Pain", "Turkey Apple Brie", "SU", "07:00:00", "22:00:00"),
    
    NewItemHour("Au Bon Pain", "Southwest Chicken", "MO", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Southwest Chicken", "TU", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Southwest Chicken", "WE", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Southwest Chicken", "TH", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Southwest Chicken", "FR", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Southwest Chicken", "SA", "07:00:00", "22:00:00"),
    NewItemHour("Au Bon Pain", "Southwest Chicken", "SU", "07:00:00", "22:00:00"),
    
    NewItemHour("Au Bon Pain", "Chicken Caesar", "MO", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Chicken Caesar", "TU", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Chicken Caesar", "WE", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Chicken Caesar", "TH", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Chicken Caesar", "FR", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Chicken Caesar", "SA", "07:00:00", "22:00:00"),
    NewItemHour("Au Bon Pain", "Chicken Caesar", "SU", "07:00:00", "22:00:00"),
    
    NewItemHour("Au Bon Pain", "The Veggie Wrap", "MO", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "The Veggie Wrap", "TU", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "The Veggie Wrap", "WE", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "The Veggie Wrap", "TH", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "The Veggie Wrap", "FR", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "The Veggie Wrap", "SA", "07:00:00", "22:00:00"),
    NewItemHour("Au Bon Pain", "The Veggie Wrap", "SU", "07:00:00", "22:00:00"),
    
    NewItemHour("Au Bon Pain", "Napa Chicken", "MO", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Napa Chicken", "TU", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Napa Chicken", "WE", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Napa Chicken", "TH", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Napa Chicken", "FR", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Napa Chicken", "SA", "07:00:00", "22:00:00"),
    NewItemHour("Au Bon Pain", "Napa Chicken", "SU", "07:00:00", "22:00:00"),
    
    NewItemHour("Au Bon Pain", "Turkey Wrap", "MO", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Turkey Wrap", "TU", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Turkey Wrap", "WE", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Turkey Wrap", "TH", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Turkey Wrap", "FR", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Turkey Wrap", "SA", "07:00:00", "22:00:00"),
    NewItemHour("Au Bon Pain", "Turkey Wrap", "SU", "07:00:00", "22:00:00"),
    
    NewItemHour("Au Bon Pain", "Tuna Wrap", "MO", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Tuna Wrap", "TU", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Tuna Wrap", "WE", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Tuna Wrap", "TH", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Tuna Wrap", "FR", "07:00:00", "24:00:00"),
    NewItemHour("Au Bon Pain", "Tuna Wrap", "SA", "07:00:00", "22:00:00"),
    NewItemHour("Au Bon Pain", "Tuna Wrap", "SU", "07:00:00", "22:00:00"),
]

for i in item_hours:
    i.save()