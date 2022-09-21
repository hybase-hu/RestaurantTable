from django.urls import path

from order.views import add_orders, delete_orders, list_orders, close_order

app_name = "orders"
urlpatterns = [

    path('add/<int:table_pk>', add_orders, name="add_orders"),
    path('closed/<int:table_order_pk>', close_order, name="close_order"),
    path('delete/<int:table_pk>/<int:order_pk>', delete_orders, name="delete_orders"),
    path('list/',list_orders,name="list_orders")
]
