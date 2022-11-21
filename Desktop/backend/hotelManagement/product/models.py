from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Customer(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.username)


# this will create token for user
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Category(models.Model):
    title = models.CharField(max_length=255, null=False)
    parent_category_id = models.IntegerField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {}".format(self.title, self.parent_category_id)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=False)
    quantity = models.IntegerField(default='0',null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {} - {}".format(self.category, self.title, self.price,self.quantity)


class Cart(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    item = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    item_quantity = models.IntegerField(null=False)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {} - {}".format(self.user, self.item, self.item_quantity)

