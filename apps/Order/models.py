from django.db import models
from apps.Menu.models import Menu


class Dish(models.Model):
    food = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class Order(models.Model):
    time = models.DateTimeField(auto_now=True)
    ref_code = models.CharField(max_length=12)
    food = models.ManyToManyField(Dish)

    def add_food(self, id):
        self.food.add(id)
