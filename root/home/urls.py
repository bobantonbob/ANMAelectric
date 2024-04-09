from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('contacts', contacts),
    path('about', about),
    path('privacy_policy', privacy_policy),
    path('warranty', warranty),
    path('orders', orders),
    path('grounding', grounding),
    path('lightning', lightning),
    path('order_ligh_groun', order_ligh_groun),
]