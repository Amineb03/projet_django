from platform import machine
from django.contrib import admin
from .models import Machine, Personnel

admin.site.register(Machine)
admin.site.register(Personnel)

# Register your models here.
