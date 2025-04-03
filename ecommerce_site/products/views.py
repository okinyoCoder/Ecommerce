from django.shortcuts import render
from .serializers import ProductSerializer, CategorySerializer, ReviewsSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveAPIView
from .models import Product, Review, Category


#create operation for all the views
class ProductCreateAPIview(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #permission_classes = [IsAdminUser]

class ReviewCreateAPIview(CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewsSerializer
