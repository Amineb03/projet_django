from platform import machine
from django.contrib import admin
from .models import Machine, Personnel, Infrastruture

admin.site.register(Machine)
admin.site.register(Personnel)  
admin.site.register(Infrastruture)

# Register your models here.
