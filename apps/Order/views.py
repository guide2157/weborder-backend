from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework import status
from hashids import Hashids

from apps.Order.models import Dish, Order


@api_view(['POST'])
def place_order(request):
    if request.method == 'POST':
        menus = request.POST.get('order')
        try:
            order = Order()
            for id in menus:
                dish = Dish.objects.create(food=id, quantity=menus[id])
                order.add_food(dish.pk)
            order.ref_code = Hashids().encode()
            order.save()
            return Response({'ref_code': order.ref_code}, status=status.HTTP_200_OK)
        except:
            return HttpResponse(status=404)
