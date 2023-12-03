"""
URL configuration for Ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
from django.urls import path
from Customer.views import CustomerListView, CustomerUpdateView, ProductListView, OrderListView, OrderUpdateView

urlpatterns = [
    path('api/customers/', CustomerListView.as_view(), name='customer-list'),
    path('api/customers/<int:pk>/', CustomerUpdateView.as_view(), name='customer-update'),
    path('api/products/', ProductListView.as_view(), name='product-list'),
    path('api/orders/', OrderListView.as_view(), name='order-list'),
    path('api/orders/<int:pk>/', OrderUpdateView.as_view(), name='order-update'),
]

