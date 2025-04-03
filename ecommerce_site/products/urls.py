from django.urls import path
from .views import ProductCreateAPIview, ReviewCreateAPIview

urlpatterns = [
    path('add-product/new/', ProductCreateAPIview.as_view(), name='create-product')
]