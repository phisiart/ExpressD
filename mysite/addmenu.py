import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django
from express.models import Type, Diner, Item
django.setup()
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

# types = [
#     Type(did=Diner.objects.filter(name="Au Bon Pain")[0], name="Sandwiches"),
#     Type(did=Diner.objects.filter(name="Au Bon Pain")[0], name="Salads"),
#     Type(did=Diner.objects.filter(name="Loop Pizza Grill")[0], name="Salads"),
#     Type(did=Diner.objects.filter(name="Loop Pizza Grill")[0], name="Pastas"),
#     Type(did=Diner.objects.filter(name="Loop Pizza Grill")[0], name="Pizza"),
#     Type(did=Diner.objects.filter(name="Twinnie's")[0], name="Sandwiches"),  
#     Type(did=Diner.objects.filter(name="Twinnie's")[0], name="Coffees"),
#     Type(did=Diner.objects.filter(name="Blue Express")[0], name="Sandwiches"),
#     Type(did=Diner.objects.filter(name="Blue Express")[0], name="Sodas"),
# ]

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

# items = [
    # Item(tid=Type.objects.filter(name="Sandwiches")[0],
    #      did=Diner.objects.filter(name="Au Bon Pain")[0],
    #      name="Turkey Club",
    #      price=1300,
    #      timeToCook=datetime.datetime.strptime("00:05:00", '%H:%M:%S').time()),
    # Item(tid=Type.objects.filter(name="Sandwiches")[0],
    #      did=Diner.objects.filter(name="Au Bon Pain")[0],
    #      name="Two Eggs Sandwiche",
    #      price=350,
    #      timeToCook=datetime.datetime.strptime("00:06:00", '%H:%M:%S').time()),
    # Item(tid=Type.objects.filter(name="Salads")[0],
    #      did=Diner.objects.filter(name="Au Bon Pain")[0],
    #      name="Tuna Salad",
    #      price=1000,
    #      timeToCook=datetime.datetime.strptime("00:04:30", '%H:%M:%S').time()),
    # Item(tid=Type.objects.filter(name="Salads")[0],
    #      did=Diner.objects.filter(name="Au Bon Pain")[0],
    #      name="Classic Chicken Salad",
    #      price=900,
    #      timeToCook=datetime.datetime.strptime("00:04:30", '%H:%M:%S').time()),
    
    # Item(tid=Type.objects.filter(name="Sandwiches")[0],
    #      did=Diner.objects.filter(name="Loop Pizza Grill")[0],
    #      name="Veggie Sandwiche",
    #      price=1000,
    #      timeToCook=datetime.datetime.strptime("00:06:00", '%H:%M:%S').time()),
    # Item(tid=Type.objects.filter(name="Pastas")[0],
    #      did=Diner.objects.filter(name="Loop Pizza Grill")[0],
    #      name="Bowtie Shrimp Pasta",
    #      price=1200,
    #      timeToCook=datetime.datetime.strptime("00:10:00", '%H:%M:%S').time()),
    # Item(tid=Type.objects.filter(name="Pastas")[0],
    #      did=Diner.objects.filter(name="Loop Pizza Grill")[0],
    #      name="Cajun Chicken Alfredo",
    #      price=1100,
    #      timeToCook=datetime.datetime.strptime("00:08:00", '%H:%M:%S').time()),
    # Item(tid=Type.objects.filter(name="Pizza")[0],
    #      did=Diner.objects.filter(name="Loop Pizza Grill")[0],
    #      name="Five Cheese Pizza",
    #      price=1600,
    #      timeToCook=datetime.datetime.strptime("00:12:00", '%H:%M:%S').time()),
    # Item(tid=Type.objects.filter(name="Pizza")[0],
    #      did=Diner.objects.filter(name="Loop Pizza Grill")[0],
    #      name="Pepperoni Pizza",
    #      price=1800,
    #      timeToCook=datetime.datetime.strptime("00:15:00", '%H:%M:%S').time()),
    
    # Item(tid=Type.objects.filter(name="Sandwiches")[0],
    #      did=Diner.objects.filter(name="Twinnie's")[0],
    #      name="Turkey Club",
    #      price=1000,
    #      timeToCook=datetime.datetime.strptime("00:06:00", '%H:%M:%S').time()),
    # Item(tid=Type.objects.filter(name="Sandwiches")[0],
    #      did=Diner.objects.filter(name="Twinnie's")[0],
    #      name="Tuna Sandwiche",
    #      price=1200,
    #      timeToCook=datetime.datetime.strptime("00:05:00", '%H:%M:%S').time()),
    # Item(tid=Type.objects.filter(name="Coffees")[0],
    #      did=Diner.objects.filter(name="Twinnie's")[0],
    #      name="Chai Latte",
    #      price=300,
    #      timeToCook=datetime.datetime.strptime("00:02:00", '%H:%M:%S').time()),
    # Item(tid=Type.objects.filter(name="Coffees")[0],
    #      did=Diner.objects.filter(name="Twinnie's")[0],
    #      name="Freshly Brew Coffee",
    #      price=200,
    #      timeToCook=datetime.datetime.strptime("00:02:00", '%H:%M:%S').time()),
    # Item(tid=Type.objects.filter(name="Sandwiches")[0],
    #      did=Diner.objects.filter(name="Blue Express")[0],
    #      name="Turkey Club",
    #      price=1000,
    #      timeToCook=datetime.datetime.strptime("00:06:00", '%H:%M:%S').time()),
    # Item(tid=Type.objects.filter(name="Sandwiches")[0],
    #      did=Diner.objects.filter(name="Blue Express")[0],
    #      name="Beef Cheese Sandwiche",
    #      price=1100,
    #      timeToCook=datetime.datetime.strptime("00:07:00", '%H:%M:%S').time()),
    # Item(tid=Type.objects.filter(name="Sodas")[0],
    #      did=Diner.objects.filter(name="Blue Express")[0],
    #      name="Coke Cola",
    #      price=200,
    #      timeToCook=datetime.datetime.strptime("00:01:00", '%H:%M:%S').time()),
    # Item(tid=Type.objects.filter(name="Sodas")[0],
    #      did=Diner.objects.filter(name="Blue Express")[0],
    #      name="Canada Dry",
    #      price=200,
    #      timeToCook=datetime.datetime.strptime("00:01:00", '%H:%M:%S').time()),
# ]



for i in items:
    i.save()
