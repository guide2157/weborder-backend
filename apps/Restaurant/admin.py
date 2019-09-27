from django.contrib import admin

from .models import Restaurant, RestaurantTag

admin.site.register(Restaurant)
admin.site.register(RestaurantTag)
