from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Reservation)
admin.site.register(models.FaqContact)
admin.site.register(models.Contact)