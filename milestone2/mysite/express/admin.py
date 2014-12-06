from django.contrib import admin
from express.models import Diner, Type, Item

# Register your models here.
admin.site.register(Diner)
admin.site.register(Type)
admin.site.register(Item)