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
