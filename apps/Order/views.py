from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import status
from hashids import Hashids
import time
from django.utils.safestring import mark_safe
import json
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

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
            order_detail = {
                'ref_code': refcode,
                'time': time.strftime("%I:%M:%S %p", time.localtime())
            }
            orders = {}

            for id in menus:
                amount = menus[id]
                menu = Menu.objects.get(id=int(id))
                orders[menu.name] = amount
                dish = Dish.objects.create(food=menu, quantity=int(amount))
                order.dish_set.add(dish)
            order_detail['orders'] = orders
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)("chat_order_list",
                                                    {'type': 'chat_message',
                                                     'message': order_detail})
            return Response({'ref_code': refcode}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return HttpResponse(status=404)

    def get(self):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders)
        return Response(serializer.data)


def room(request, room_name):
    return render(request, 'room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })
