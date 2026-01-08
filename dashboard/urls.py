from django.urls import path
from . import views  # Import all views from this app

urlpatterns = [
    path('', views.dashboard_home, name='dashboard'),        # Dashboard home
    path('orders/', views.orders_page, name='orders'),        # Orders page
    path('products/', views.products_page, name='products'),  # Products page
    path('customers/', views.customers_page, name='customers'),  # Customers page
]
