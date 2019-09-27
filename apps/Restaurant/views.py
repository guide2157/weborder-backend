from .models import Menu
from .models import Restaurant
from .serializers import RestaurantSerializer
from ..Menu.serializers import MenuSerializer
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class RestaurantView(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    lookup_fields = ('id', 'slug')

    def get_featured_menus(self, menus):
        featured_menus = []
        for menu_group in menus:
            menu_data = MenuSerializer(menu_group).data

            if menu_data is not None:
                featured_menus.append(menu_data)

        return featured_menus

    def get(self, request, **kwargs):
        queryset = self.get_queryset()
        filter_obj = {}
        keys_map = {'id': 'object_pk', 'slug': 'slug'}

        for field in self.lookup_fields:
            if self.kwargs.get(field, None) is not None:
                filter_obj[keys_map[field]] = self.kwargs[field]

        obj = get_object_or_404(queryset, **filter_obj)

        restaurant_serializer = RestaurantSerializer(obj)

        featured_menu_serializer = self.get_featured_menus(obj.featured_menus.all())

        payload = {
            **restaurant_serializer.data,
            'featured_menus': featured_menu_serializer
        }

        return Response(payload, status=200, **kwargs)
