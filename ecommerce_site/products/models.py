from django.db import models

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