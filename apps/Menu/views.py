from .models import Menu
from .serializers import MenuSerializer
from rest_framework import generics


class MenuList(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
