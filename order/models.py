from django.db import models

# Create your models here.
from food.models import Food
from table.models import Table


class Order(models.Model):
    food = models.ForeignKey(Food, on_delete=models.SET_NULL, null=True)
    count = models.IntegerField(blank=False, null=False, default=1)
    created_at = models.DateTimeField(auto_created=True, auto_now_add=True)

    def __str__(self):
        return "[" + str(self.count) + "]" + self.food.name

    def get_price(self):
        return self.food.price * self.count


class TableOrder(models.Model):
    orders = models.ManyToManyField(to=Order)
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True,related_name="tables_orders")
    is_finished = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_created=True, auto_now_add=True)

    def __str__(self):
        return str(self.table) + "[ " + str(self.orders.count()) + " cnt]" + " [ " + str(self.get_price()) + " FT]"

    def get_price(self):
        price = 0
        for o in self.orders.all():
            price += o.food.price * o.count
        return price
