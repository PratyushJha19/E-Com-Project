from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('base/', views.base, name='base'),
]
