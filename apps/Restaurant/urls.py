from django.conf.urls import url
from .views import RestaurantView

urlpatterns = [
    url(r'^info/', RestaurantView.as_view(), name='restaurant_info'),
]