from django.contrib import admin
from remate_django_baseapp.models import Customer, MenuItem, OrderDate
from .models import UserProfileInfo, User

# Register your models here.

admin.site.register(Customer)
admin.site.register(MenuItem)
admin.site.register(OrderDate)
admin.site.register(UserProfileInfo)
