from django.db import models
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=256)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    image_url = models.ImageField(upload_to='product_photos/')
    created_date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name

#class Order(models.Model):
    #user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='orders')
    #OrderItem =models.ForeignKey(OrderItem, on_delete=models.CASCADE, related_name='orders')
    #created_date = models.DateTimeField(auto_now_add=True)
    #status = models.BooleanField(default=False)

#class OrderItem(models.Model):
    #order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    #product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='items')
    #quantity = models.PositiveIntegerField()
    #cost = models.DecimalField(max_digits=10, decimal_places=2)
    #def __str__(self):
        #return f"{self.quantity} x {self.product.name}"

#class Pay(models.Model):
    #order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='payments')
    #user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='payments')
    #total_price = models.DecimalField(max_digits=10, decimal_places=2)
    #created_date = models.DateTimeField(auto_now_add=True)  
    #status = models.BooleanField(default=False)

    #def __str__(self):
        #return f"Payment for {self.order.id}"

class Review(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reviews')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    rating = models.SmallIntegerField()
    comment = models.TextField(max_length=256)
    created_date = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"Review by {self.user.username} on {self.product.name}"