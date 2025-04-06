from django.shortcuts import render
from .serializers import ProductSerializer, CategorySerializer, ReviewsSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveAPIView
from .models import Product, Review, Category
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from drf_spectacular.utils import extend_schema, extend_schema_view

@extend_schema_view(
    list=extend_schema(description='Get a list of all categories'),
    retrieve=extend_schema(description='Get details of a specific category'),
    create=extend_schema(description='Create a new category'),
    update=extend_schema(description='Update an existing category'),
    destroy=extend_schema(description='Delete a category')
)

#CRUD operation for all the Product views
@extend_schema_view(
    list=extend_schema(
        description='Get a list of all Ecommerce products',
        responses={200: ProductSerializer(many=True)}
    ),
    retrieve=extend_schema(
        description='Get details of a specific Ecommerce product',
        responses={200: ProductSerializer}
    ),
    create=extend_schema(
        description='Create a Ecommerce products',
        responses={201: ProductSerializer}
    ),
    destroy=extend_schema(
        description='Delete a Ecommerce product',
        responses={204: None}
    )
)
class ProductCreateAPIview(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
   
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
@extend_schema_view(
    list=extend_schema(
        description='Get a list of all Ecommerce products Reviews',
        responses={200: ReviewsSerializer(many=True)}
    ),
    retrieve=extend_schema(
        description='Get details of a specific Ecommerce product Review',
        responses={200: ReviewsSerializer}
    ),
    create=extend_schema(
        description='Create a Ecommerce products Review',
        responses={201: ReviewsSerializer}
    ),
    destroy=extend_schema(
        description='Delete a Ecommerce product Review',
        responses={204: None}
    )
)
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

#CRUD operation for Reviews Category
@extend_schema_view(
    list=extend_schema(description='Get a list of all categories'),
    retrieve=extend_schema(description='Get details of a specific category'),
    create=extend_schema(description='Create a new category'),
    update=extend_schema(description='Update an existing category'),
    destroy=extend_schema(description='Delete a category')
)
class CategoryCreateAPIview(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]

class CategoryDestroyAPIView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]

class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer