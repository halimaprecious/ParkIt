from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(Profile)
admin.site.register(Parkslot)
admin.site.register(Payment)
admin.site.register(Booking)


