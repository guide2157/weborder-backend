from django.conf.urls import url
from .views import place_order, room

urlpatterns = [
    url(r'^place/', place_order.as_view(), name='place_order'),
    url(r'^(?P<room_name>\w+)/', room, name='room'),
]
