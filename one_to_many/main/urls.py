from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process_chef', views.process_chef),
    path('process_dish', views.process_dish),
]
