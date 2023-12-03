from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    contact_number = models.CharField(max_length=10)
    email = models.EmailField(unique=True)


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2,
                                 validators=[MinValueValidator(0), MaxValueValidator(25)])


class Order(models.Model):
    order_number = models.CharField(max_length=10, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateField()
    address = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        if not self.order_number:
            last_order = Order.objects.order_by('-id').first()
            if last_order:
                last_order_number = int(last_order.order_number[3:])
                new_order_number = f"ORD{last_order_number + 1:05}"
            else:
                new_order_number = "ORD00001"

            self.order_number = new_order_number

        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number

    class Meta:
        ordering = ['-id']


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_item', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
