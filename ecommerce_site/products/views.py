from django.shortcuts import render
from .serializers import ProductSerializer, CategorySerializer, ReviewsSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveAPIView
from .models import Product, Review, Category
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


#CRUD operation for all the Product views
class ProductCreateAPIview(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]
   
class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category', 'stock_available']
    search_fields = ['name', 'price']

class ProductRetrieveAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDestroyAPIView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser] 

#CRUD operation for Reviews view
class ReviewCreateAPIview(CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewsSerializer
    permission_classes = [IsAuthenticated]


class ReviewListAPIView(ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewsSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['user']
    ordering_fields = ['created_date']

class ReviewRetrieveAPIView(RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewsSerializer

class ReviewDestroyAPIView(DestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewsSerializer
    permission_classes = [IsAuthenticated]