from django.urls import path
from . import views

urlpatterns = [
    path('register/create/',  views.register_view, name='create-user'),
    path('login/', views.login_view, name='user-login')
]