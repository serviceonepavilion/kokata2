from django.db import models
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import User
from accounts.models import Profile


class Menu(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=2080)
    inStock = models.BooleanField(default=True)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=10)
    order_completed = models.BooleanField(default=False)
    ordered_date = models.DateField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.profile.user.username

    def totalprice(self):
        return int(self.item.price) * int(self.quantity)


class Timing(models.Model):
    shop_open = models.TimeField(default=None)
    shop_close = models.TimeField(default=None)
    open_now = models.BooleanField(default=True)
