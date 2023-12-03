from django.utils import timezone
import pytz
from rest_framework import serializers
from .models import Customer, Product, Order, OrderItem


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        extra_kwargs = {
            'name': {'validators': []},
            'email': {'validators': []},
        }

    def validate_name(self, value):
        if Customer.objects.filter(name=value).exists():
            raise serializers.ValidationError("A customer with this name already exists.")
        return value


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        extra_kwargs = {
            'name': {'validators': []},
            'weight': {'validators': []},
        }

    def validate_weight(self, value):
        if value > 25:
            raise serializers.ValidationError("Weight cannot be more than 25kg.")
        return value

    def validate_name(self, value):
        if Product.objects.filter(name=value).exists():
            raise serializers.ValidationError("A product with this name already exists.")
        return value


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    order_item = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['order_number', 'customer', 'order_date', 'address', 'order_item']
        extra_kwargs = {
            'order_number': {'read_only': True},
        }

    def create(self, validated_data):
        order_items_data = validated_data.pop('order_item', [])

        order = Order.objects.create(**validated_data)
        for order_item_data in order_items_data:
            product = order_item_data['product']
            quantity = order_item_data['quantity']
            OrderItem.objects.create(order=order, product=product, quantity=quantity)

        return order

    def update(self, instance, validated_data):
        instance.customer = validated_data.get('customer', instance.customer)
        instance.order_date = validated_data.get('order_date', instance.order_date)
        instance.address = validated_data.get('address', instance.address)
        instance.save()

        order_items_data = validated_data.get('order_item', [])
        instance.order_item.all().delete()

        for order_item_data in order_items_data:
            product = order_item_data['product']
            quantity = order_item_data['quantity']
            OrderItem.objects.create(order=instance, product=product, quantity=quantity)

        return instance

    def validate_order_date(self, value):
        ist_timezone = pytz.timezone('Asia/Kolkata')
        now_ist = timezone.now().astimezone(ist_timezone).date()
        if value < now_ist:
            raise serializers.ValidationError("Order Date cannot be in the past.")
        return value

    def validate_order_item(self, value):
        total_weight = sum(item['product'].weight * item['quantity'] for item in value)
        if total_weight >= 150:
            raise serializers.ValidationError("Order cumulative weight must be under 150kg.")
        return value
