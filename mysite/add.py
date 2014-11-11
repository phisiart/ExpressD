import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

from express.models import *


diners = [
    Diner(name="Blue Express", loc="LSRC"),
]

for diner in diners:
    diner.save()
