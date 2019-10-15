from django.db import models
from apps.Menu.models import Menu


class Dish(models.Model):
    food = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.food.name + " : " + str(self.quantity)


class Order(models.Model):
    time = models.DateTimeField(auto_now=True)
    ref_code = models.CharField(max_length=12)
    food = models.ManyToManyField(Dish)

    def __str__(self):
        return self.ref_code

