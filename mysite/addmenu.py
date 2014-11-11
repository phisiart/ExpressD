import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django
from express.models import Type, Diner, Item
django.setup()
import datetime

types = [
    Type(did=Diner.objects.filter(name="Au Bon Pain")[0], name="Sandwiches"),
]

for t in types:
    t.save()

items = [
    Item(tid=Type.objects.filter(name="Sandwiches")[0],
         did=Diner.objects.filter(name="Au Bon Pain")[0],
         name="Turkey Club",
         price=1300,
         timeToCook=datetime.datetime.strptime("00:05:00", '%H:%M:%S').time())
]



for i in items:
    i.save()
