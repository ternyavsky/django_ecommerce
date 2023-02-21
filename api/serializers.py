from rest_framework import serializers
from main.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title','price','text']

    def create(self,validate_data):
        print(validate_data)
        return Product.objects.create(**validate_data)
