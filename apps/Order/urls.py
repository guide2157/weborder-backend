from django.conf.urls import url
from .views import place_order

urlpatterns = [
    url(r'^', place_order, name='place_order'),
]