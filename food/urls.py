from django.urls import path

from food.views import add_food
from order.views import add_orders, delete_orders

app_name = "food"
urlpatterns = [

    path('add/', add_food, name="add_food"),

]