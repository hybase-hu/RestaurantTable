from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from RestaurantTable.static_strings import ALL_ORDERS_DELETE
from order.forms import OrderForm
from order.models import TableOrder, Order
from order.utils import html_to_pdf

from table.models import Table


def add_orders(request, table_pk):
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        table_order = TableOrder.objects.filter(table=table_pk, is_finished=False).first()
        if order_form.is_valid():
            try:
                order = order_form.save()
            except Exception as e:
                messages.warning(request,e)
                return redirect("table:table_view", pk=table_pk)



            if table_order is not None:
                table_order.orders.add(order)
                table_order.save()
            else:
                table = Table.objects.get(pk=table_pk)
                table_order = TableOrder(table=table)
                table_order.save()
                table_order.orders.add(order)
                table_order.save()

    return redirect("table:table_view", pk=table_pk)


def delete_orders(request,table_pk,order_pk):
    if request.method == "POST":
        order = Order.objects.get(pk=order_pk)
        table_order = TableOrder.objects.filter(table__id=table_pk, is_finished=False).first()
        table_order.orders.remove(order)
        table_order.save()

        if table_order.orders.count() < 1:
            table_order.delete()
            messages.success(request,ALL_ORDERS_DELETE)
            return redirect("/")

        order.delete()

    return redirect("table:table_view", pk=table_pk)


def list_orders(request):
    current_table_orders = TableOrder.objects.filter(is_finished=False)

    context = {
        "current_table_orders":current_table_orders
    }
    return render(request,'order/list_orders.html',context)


def close_order(request,table_order_pk):
    table_order = TableOrder.objects.get(pk=table_order_pk)
    context = {
        'table_order':table_order
    }
    print(context)
    pdf = html_to_pdf(template_src='order/block.html',context_dict=context)
    response = HttpResponse(pdf,content_type='application/file')
    response['Content-Disposition'] = 'filename="report.pdf";attachment'


    if response is not None:
        table_order.is_finished = True
        table_order.save()
        #messages.success(request,"This table orders is finished")



    return response
