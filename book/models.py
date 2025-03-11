from django.db import models
from main.models import Book


class Cart(models.Model):
    session_id = models.CharField(max_length=128)
    session_at = models.DateTimeField(auto_now=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_price(self):
        return self.book.price * self.quantity

    def __str__(self):
        return f"{self.book.name} x {self.quantity}"
