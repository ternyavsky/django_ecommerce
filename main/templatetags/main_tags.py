from django import template
register = template.Library()
from main.cart import Cart
from main.models import Product
from django.contrib.auth.decorators import login_required

@register.simple_tag(name='cart')
def get_quantity(request):
    cart = Cart(request)
    return cart.get_quantity()


