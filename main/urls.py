from django.urls import path
from . import views
from .models import Product



urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('contact',views.Contact.as_view(),name='contact'),
    path('about',views.AboutView.as_view(),name='about'),
    path('products',views.ProductView.as_view(),name='product'),
    path('services',views.ServiceView.as_view(),name='service'),
    path('single<int:id>/',views.ProductSingle.as_view(),name='single'),

    path('cart',views.CartView.as_view(),name='cart'),
    path('cart_add<int:product_id>',views.cart_add,name='cart_add'),
    path('checkout',views.CheckoutView.as_view(),name='checkout'),
    path('create_order',views.create_order,name='create_order'),
    
    path('account<int:id>/',views.AccountView.as_view(),name='account'),


    path('add<int:product_id>',views.move_add,name='move_add'),
    path('remove<int:product_id>',views.move_remove,name='move_remove'),

    

]
