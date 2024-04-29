from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Restaurant)
admin.site.register(models.Customer)
admin.site.register(models.Reservations)
admin.site.register(models.Membership)
