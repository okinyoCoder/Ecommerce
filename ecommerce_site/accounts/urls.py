from django.urls import path
from . import views

urlpatterns = [
    path('user/new/', views.register_view, name='create-user'),
    path('user/login/', views.login_view, name='user-login'),
]