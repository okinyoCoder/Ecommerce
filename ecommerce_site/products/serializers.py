from rest_framework import serializers
from . models import Review, Product, Category

class ReviewsSerializer(serializers.Serializer):
    class meta:
        model = Review
        fields = ['id', 'user', 'product', 'comment', 'created_date']

class ProductSerializer(serializers.Serializer):
    reviews = ReviewsSerializer(many=True, read_only=True)
    class meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock', 'image_url', 'created_date', 'reviews']

class CategorySerializer(serializers.Serializer):
    products = ProductSerializer(many=True, read_only=True)
    class meta:
        model = Category
        fields = ['id', 'name', 'products']