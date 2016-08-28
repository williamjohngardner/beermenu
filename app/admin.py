from django.contrib import admin

from app.models import Beer, Restaurant, UserProfile



class BeerAdmin(admin.ModelAdmin):
    list_display = ('beer_name', 'brewer_name', 'beer_type', 'abv')

admin.site.register(Beer, BeerAdmin)

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')

admin.site.register(Restaurant, RestaurantAdmin)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ( 'user', 'user_name', 'first_name', 'last_name', 'email')

admin.site.register(UserProfile, UserProfileAdmin)
