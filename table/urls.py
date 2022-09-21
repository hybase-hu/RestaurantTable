from django.contrib import admin
from django.urls import path

from table.views import home, table_view, table_close

app_name="table"
urlpatterns = [
   path("",home,name="home"),
   path('table/<int:pk>',table_view,name="table_view"),
   path('table/close/<int:pk>',table_close,name="table_close"),
]