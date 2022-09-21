from django.db import models



# ez megint a körkörös beágyazás miatt kellett így
from order import models as TableOrderModels


class Table(models.Model):
    t_id = models.IntegerField(null=False,blank=False,unique=True)
    description = models.TextField(blank=True,null=True)
    is_reserved = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.t_id) + " [" + self.description[:25] + "]"

    def get_available_tables():
        return Table.objects.filter(is_active=True,is_reserved=False)

    def get_table_order_count(self):
        count = 0
        for i in self.get_table_current_orders():
            for k in i.orders.all():
                count += 1
        return count


    def get_table_order_price(self):
        table_orders = TableOrderModels.TableOrder.objects.filter(table=self.pk,is_finished=False)
        price = 0.0
        for o in table_orders:
            price += o.get_price()

        return price

    def get_table_current_orders(self):
        tableOrders=TableOrderModels.TableOrder.objects.filter(table=self.pk,is_finished=False)

        return tableOrders