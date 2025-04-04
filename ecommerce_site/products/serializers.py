from rest_framework import serializers
from . models import Review, Product, Category
from django.contrib.auth import get_user_model

class ReviewsSerializer(serializers.ModelSerializer):
    user = get_user_model()
    class Meta:
        model = Review
        fields = ['id', 'user', 'comment', 'created_date']

class ProductSerializer(serializers.ModelSerializer):
    reviews = ReviewsSerializer(many=True, read_only=True)
    stock_available = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock', 'image_url', 'created_date', 'reviews', 'stock_available']

        def get_stock_available(self, data):
            if data['stock'] < 1:
                return False

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['id', 'name', 'products']