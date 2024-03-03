from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('contacts', contacts),
    path('about', about),
    path('privacy_policy', privacy_policy),
    path('warranty', warranty),
    path('orders', orders),

]