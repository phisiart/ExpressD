import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

from express.models import *

types = [
    Type(did=Diner.objects.filter(name="Au Bon Pain")[0].did, name="Sandwiches"),

]

items = [
    Item(tid=Type.objects.filter(name="Sandwiches")[0].tid,
         did=Diner.objects.filter(name="Au Bon Pain")[0].did,
         name="Turkey Club",
         price=1300
         timeToCook=datetime.datetime.strptime("00:05:00", '%H:%M:%S').time())
]

for diner in diners:
    diner.save()