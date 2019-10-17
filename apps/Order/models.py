from django.db import models
from apps.Menu.models import Menu


class Order(models.Model):
    time = models.DateTimeField(auto_now=True)
    ref_code = models.CharField(max_length=12)

    def __str__(self):
        return self.ref_code


class Dish(models.Model):
    food = models.ForeignKey(Menu, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.food.name + " : " + str(self.quantity)



