from django.urls import path
from .views import (
    ProductCreateAPIview, ProductListAPIView, ProductRetrieveAPIView, ProductDestroyAPIView,
    ReviewCreateAPIview, ReviewListAPIView, ReviewRetrieveAPIView, ReviewDestroyAPIView,
    CategoryListAPIView, CategoryDestroyAPIView, CategoryCreateAPIview
)

urlpatterns = [
    # Product Endpoints
    path('products/', ProductListAPIView.as_view(), name='product-list'),
    path('products/create/', ProductCreateAPIview.as_view(), name='product-create'),
    path('products/<int:pk>/', ProductRetrieveAPIView.as_view(), name='product-detail'),
    path('products/<int:pk>/delete/', ProductDestroyAPIView.as_view(), name='product-delete'),

    # Review Endpoints
    path('reviews/', ReviewListAPIView.as_view(), name='review-list'),
    path('reviews/create/', ReviewCreateAPIview.as_view(), name='review-create'),
    path('reviews/<int:pk>/', ReviewRetrieveAPIView.as_view(), name='review-detail'),
    path('reviews/<int:pk>/delete/', ReviewDestroyAPIView.as_view(), name='review-delete'),

    # Category Endpoints
    path('categorys/', CategoryListAPIView.as_view(), name='review-list'),
    path('categorys/create/', CategoryCreateAPIview.as_view(), name='review-create'),
    path('categorys/<int:pk>/delete/', CategoryDestroyAPIView.as_view(), name='review-delete'),
]