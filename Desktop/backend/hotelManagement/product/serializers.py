from datetime import datetime
from rest_framework import serializers
from product.models import Cart, Category, Customer, Product


class CustomerSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Customer
        fields = ("id", "username", "first_name", "last_name", "email", "password")

    def create(self, validated_data):
        user = super(CustomerSerializer, self).create(validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ["id", "user", "item","item_quantity","is_deleted", "created_at", "updated_at"]
        


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "title", "parent_category_id","is_deleted", "created_at", "updated_at"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "title", "category", "quantity", "is_deleted","price", "created_at", "updated_at"]
        