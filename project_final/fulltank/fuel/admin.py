from django.contrib import admin

from .models import FuelConsumption, FCShort, Price, Cities, States

admin.site.register(FuelConsumption)
admin.site.register(FCShort)
admin.site.register(Price)
admin.site.register(Cities)
admin.site.register(States)