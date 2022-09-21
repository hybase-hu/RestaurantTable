from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
# Create your views here.
from RestaurantTable.static_strings import ALL_ORDERS_DELETE
from order.forms import OrderForm
from order.models import TableOrder, Order
from table.models import Table


def home(request):
    tables = Table.get_available_tables()
    context = {
        'tables': tables
    }
    return render(request, 'table/tables.html', context)


def table_view(request, pk):
    table = Table.objects.get(pk=pk)
    order_form = OrderForm()
    context = {
        'table': table,
        'form':order_form
    }

    if request.method == "POST":
        if "add" in request.POST and request.POST['add'] == "xcv":
            table_order = TableOrder.objects.get(pk=request.POST['table_orders_pk'])
            order = Order.objects.get(pk=request.POST['order_pk'])
            if order is not None:
                order.count += 1
                order.save()

        if "minus" in request.POST and request.POST['minus'] == "xvv":
            order = None
            table_order=None

            try:
                table_order = TableOrder.objects.get(pk=request.POST['table_orders_pk'])
                order = Order.objects.get(pk=request.POST['order_pk'])
                print("order count:", table_order.orders.count(), "order:", order)
            except:
                messages.warning(request,"This orders is not available")

            if order is not None:
                if order.count >= 1:
                    print("order count:",order.count)
                    order.count -= 1
                    order.save()
                    print("order delete:", order.count)
                if order.count == 0:
                    order.delete()
                    print("order count now:", order.count)
                    table_order.orders.remove(order)
                    print("orders delete from tableorder:", order.count)
                    table_order.save()
                    print("table orders count is ",table_order.orders.count())
                    if table_order.orders.count() == 0:
                        table_order.delete()
                        messages.success(request,ALL_ORDERS_DELETE)

                        return redirect("/")

    return render(request, 'table/table_view.html', context)


def table_close(request,pk):
    pass
