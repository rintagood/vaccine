from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [

    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('kasargod',views.kasargod,name='kasargod'),
    path('kannur',views.kannur,name='kannur'),
    path('kozhikode',views.kozhikode,name='kozhikode'),
    path('wayanad',views.wayanad,name='wayanad'),
    path('malappuram',views.malappuram,name='malappuram'),
    path('palakkad',views.palakkad,name='palakkad'),
    path('kochi',views.kochi,name='kochi'),
    path('tvm',views.tvm,name='tvm'),
    path('slot',views.slot,name='slot'),
    ]