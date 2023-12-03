from django.shortcuts import render
from rest_framework import generics
from .models import Customer, Product, Order
from .serializers import CustomerSerializer, ProductSerializer, OrderSerializer


class CustomerListView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderListView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        products = self.request.query_params.get('products')
        if products:
            products_list = products.split(',')
            queryset = queryset.filter(order_item__product__name__in=products_list)

        customer = self.request.query_params.get('customer')
        if customer:
            queryset = queryset.filter(customer__name=customer)

        return queryset


class OrderUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
