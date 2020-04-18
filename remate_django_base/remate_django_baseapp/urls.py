from django.urls import path
from . import views

# SET THE NAMESPACE!
app_name = 'remate_django_baseapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('customers/',views.customers,name='customers'),
    path('other/',views.other,name='other'),
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
    path('user_logout/',views.user_logout,name='user_logout'),
]
