from typing import Any, Dict
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.views.generic import CreateView,TemplateView,DetailView,ListView
from .models import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.mail import send_mail
from rest_framework.views import APIView
from api.serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from .cart import Cart
import random
from django.contrib import messages


# Home view, "preview_objects" - products for carousel, products - all products

class HomeView(TemplateView):
    template_name = "main/index.html"
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['preview_objects'] = Product.objects.all()[:3]
        context['products'] = Product.objects.all()
        return context


class CheckoutView(TemplateView):
    template_name = "main/checkout.html"

    def post(self,request):
        new_address = UserAddress.objects.create(
            address=request.POST.get('address'),
            city=request.POST.get('city'),
            state=request.POST.get('state'),
            zip_code=request.POST.get('zipcode'),
            user=request.user)
        print(new_address)
        return redirect 
    

    def get(self,request):
        try:
            order = Order.objects.get(user=request.user)
        except:
            order = None
        if order is not None:
            messages.error(request,'Pay for an existing order first or cancel it')
            return redirect('cart')
        
        cart = Cart(request).get_quantity()
        if cart == 0:
            messages.error(request,'You cart is empty!')
            return redirect('cart')
        try:
            address = UserAddress.objects.get(user=self.request.user.id)
        except:
            address = None
        context = {
            'cart':Cart(request),
            'status_address':address
        }

        return render(request,self.template_name,context=context)
    




    

# Products view, All products
class ProductView(ListView):
    template_name = "main/product.html"
    model = Product
    context_object_name = "products"

# About view
class AboutView(TemplateView):
    template_name = "main/about.html"


# Service view
class ServiceView(TemplateView):
    template_name = "main/services.html"

# Contact view
class Contact(TemplateView):
    template_name = 'main/contact.html'
    
    @method_decorator(login_required)
    def post(self, request) -> HttpResponse:
        subject = request.POST.get('subject')
        text = request.POST.get('message')
        user = User.objects.all()
        users_emails = [i.email for i in user]
        print(users_emails)
        send_mail(subject,text,'ternyavsky2016@yandex.ru',[request.user.email])
        return redirect('about')


# Cart view
class CartView(TemplateView):
    template_name = "main/cart.html"
    
    def get_context_data(self,*args,**kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['cart'] = Cart(self.request)
        return context
    
# Account view    
class AccountView(TemplateView):
    template_name = "registration/account.html"

    def get_context_data(self,id, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['user'] = User.objects.get(id=id)
        return context


#Unique product and his feedbacks in 
class ProductSingle(TemplateView):
    template_name = "main/single.html"
    def get_context_data(self,id, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)    
        context['product'] = Product.objects.get(id=id)
        context['feedback'] = Feedback.objects.filter(feedback=id)
        return context
    
    def post(self,request,id):
        author = request.user
        text = request.POST.get('text')
        product = Product.objects.get(id=id)
        Feedback.objects.create(author=author,text=text,feedback=product) 
        return redirect('single',product.id)


class ProductApiList(APIView):
    def post(self,request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post':serializer.data, 'status':200})
    
    def get(self,request):
        product = Product.objects.all()
        serializer = ProductSerializer(product,many=True)
        return Response(serializer.data)


###   GROUP METHODS ADD/REMOVE ITEM ON CART ###
# Add item from product or уебать димана home page
@login_required
def cart_add(request,product_id):
    item = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.add(request=request,product=item)
    return redirect('product')

# Add item's quantity from cart 
@login_required
def move_add(request,product_id):
    item = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.move_add(product=item)
    return redirect('cart')


# Remove item's quantity from cart
@login_required
def move_remove(request,product_id):
    item = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.move_remove(product=item)
    return redirect('cart')


@login_required
def create_order(request):
    try:
        cart = Cart(request)
        order = Order.objects.create(
            user=request.user,
            address=UserAddress.objects.get(user=request.user),
            order_id=random.randint(1000000,1999999),
            price=cart.get_total_price())
        for item in cart:
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                price=item['price'],
                quantity=item['quantity'])
        cart.clear()
        return redirect('home')
    except:
        messages.error(request,'Address not found!')
        return redirect('checkout')










