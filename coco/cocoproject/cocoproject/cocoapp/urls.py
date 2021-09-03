
from django.urls import path
from . import views
app_name='cocoapp'

urlpatterns = [
    path('',views.index,name='index'),

]