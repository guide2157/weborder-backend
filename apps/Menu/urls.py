from django.conf.urls import url
from .views import MenuList

urlpatterns = [
    url(r'^all/', MenuList.as_view(), name='all_menus'),
]