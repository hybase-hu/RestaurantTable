from django.contrib import messages
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView, CreateView

from RestaurantTable.static_strings import ADD_FOOD_SUCCESS
from food.forms import FoodForm


def add_food(request):
    form = FoodForm()
    context = {
        'form':form
    }
    if request.method == "POST":
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request,ADD_FOOD_SUCCESS)
        else:
            messages.warning(request,"error")


    return render(request,'food/add_food.html',context)