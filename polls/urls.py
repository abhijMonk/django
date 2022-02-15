from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('mypath/', views.index, name='index'),
    path('mypath2/', views.index, name='index'),
]