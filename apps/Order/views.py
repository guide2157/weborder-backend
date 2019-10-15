from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import status
from hashids import Hashids
import time

from apps.Menu.models import Menu
from apps.Order.models import Dish, Order
from apps.Order.serializers import OrderSerializer


class place_order(APIView):
    permission_classes = [AllowAny]
    queryset = Order.objects.all()

    def post(self, request):
        menus = request.data.get('order')
        try:
            refcode = Hashids(salt='guide').encode(int(time.time()))
            order = Order.objects.create(
                ref_code=refcode
            )
            for id in menus:
                amount = menus[id]
                menu = Menu.objects.get(id=int(id))
                dish = Dish.objects.create(food=menu, quantity=int(amount))
                order.food.add(dish.pk)
            return Response({'ref_code': refcode}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return HttpResponse(status=404)

    def get(self):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders)
        return Response(serializer.data)
