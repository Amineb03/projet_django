from platform import machine
from django.contrib import admin
from .models import Machine, Partenaires, Personnel, Infrastruture

admin.site.register(Machine)
admin.site.register(Personnel)  
admin.site.register(Infrastruture)
admin.site.register(Partenaires)

# Register your models here.
