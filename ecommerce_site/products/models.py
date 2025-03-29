from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
#Description, Price, Category, Stock Quantity, Image URL, and Created Date.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        """
        Creates and saves a User with the given email, other_fields and password.
        """
        if not email:
            raise ValueError('User must have an email')
        user = self.model(email=self.normalize_email(email), password=password, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given email, other_fields and password.
        """
        user = self.create_user(email, password=password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    email = models.EmailField(verbose_name="email address", unique=True, max_length=255)
    username = models.TextField(max_length=256)


    def __str__(self):
        return self.username
    
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'


class Product(models.Model):
    class Categ(models.TextChoices):
        Elec = 'lectronic'
        Pers ='personal care'
        Gro = 'grocery'
        Foo ='food'
        Clo ='clothing' 

    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=256, blank=False, null=False)
    price = models.DecimalField(decimal_places=3)
    stock = models.IntegerField()
    image_url = models.ImageField(upload_to='profile_photos/')
    category = models.CharField( max_length=3, choices=Categ, default=Categ.Foo)
    created_date = models.DateField(auto_created=True)

class OrderItem(models.model):
    product_item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    cost = models.DecimalField(decimal_places=3)

class Pay(models.model):
    order = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    total_price = models.DecimalField(decimal_places=3) 
    created_date = models.DateField(auto_created=True)
    status = models.BooleanField(default=False)

class Review(models.Model):
    ...