from main.models import Product
from decimal import Decimal
from django.conf import settings

class Cart():
    

    def __init__(self,request):
        self.session = request.session
        try:
            self.cart = self.session['cart']
        except KeyError:
            self.cart = self.session['cart'] = {}

    def add(self,request,product):
        id = str(product.id)
        if id not in self.cart:
            self.cart[id] = {'quantity': 1,'price':str(product.price)}
            self.save()
        else:
            self.cart[id]['quantity'] += 1
        self.save()


    def save(self):
        self.session['cart'] = self.cart
        self.session.modified = True


    def info(self):
        return self.cart
    
    
    def move_add(self,product):
        self.cart[str(product.id)]['quantity'] += 1
        self.save()
    
    
    def move_remove(self,product):
        if self.cart[str(product.id)]['quantity'] == 1:
            del self.cart[str(product.id)]
            self.save()
        else:
            self.cart[str(product.id)]['quantity'] -= 1
            self.save() 

    
    def get_quantity(self):
        return sum([item['quantity'] for item in self.cart.values()]) 

    
    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product


        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            yield item


    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())


    def clear(self):
        del self.session['cart']
        self.session.modified = True