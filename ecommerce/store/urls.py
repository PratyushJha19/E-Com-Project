from django.urls import path
from . import views

urlpatterns = [
    # Store main page
    path('', views.store, name='store'),

    # Indivisual Product
    path('product/<slug:product_slug>/', views.product_info, name='product_info'),

    # Main page category wise
    path('search/<slug:category_slug>', views.list_category, name='list_category')
]
