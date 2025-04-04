from django.urls import path
from .views import (
    ProductCreateAPIview, ProductListAPIView, ProductRetrieveAPIView, ProductDestroyAPIView,
    ReviewCreateAPIview, ReviewListAPIView, ReviewRetrieveAPIView, ReviewDestroyAPIView
)

urlpatterns = [
    # Product Endpoints
    path('add-product/new/', ProductCreateAPIview.as_view(), name='create-product'),
        path('products/', ProductListAPIView.as_view(), name='product-list'),
    path('products/create/', ProductCreateAPIview.as_view(), name='product-create'),
    path('products/<int:pk>/', ProductRetrieveAPIView.as_view(), name='product-detail'),
    path('products/<int:pk>/delete/', ProductDestroyAPIView.as_view(), name='product-delete'),

    # Review Endpoints
    path('reviews/', ReviewListAPIView.as_view(), name='review-list'),
    path('reviews/create/', ReviewCreateAPIview.as_view(), name='review-create'),
    path('reviews/<int:pk>/', ReviewRetrieveAPIView.as_view(), name='review-detail'),
    path('reviews/<int:pk>/delete/', ReviewDestroyAPIView.as_view(), name='review-delete'),
]