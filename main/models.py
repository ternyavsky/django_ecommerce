from django.db import models
from django.contrib.auth.models import AbstractUser, User



class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    text = models.TextField(max_length=1000)
    image = models.ImageField(null=True, blank=True,default=None)
    

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Feedback(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    text = models.CharField(max_length=255)
    feedback = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.author} - {self.text}'


class UserAddress(models.Model):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.IntegerField(null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    
    
    def __str__(self):
        return f'{self.user} - {self.address}'
    

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    address = models.ForeignKey(UserAddress, on_delete=models.CASCADE,null=True,blank=True)
    order_id = models.IntegerField()
    price = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Order №{self.order_id}'
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.order} Product:{self.product}, Quantity:{self.quantity}'
    
    

    


