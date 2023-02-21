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



