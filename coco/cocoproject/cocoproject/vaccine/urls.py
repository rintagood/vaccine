from django.contrib import admin
from django.urls import path
from . import views
app_name='vaccine'


urlpatterns = [

    path('base',views.base,name='base'),
    path('load-centers/',views.load_centers,name='ajax_load_centers'),
    ]