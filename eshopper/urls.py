from django.urls import path
from . import views
from .views import Search

urlpatterns = [
    path('', views.index, name = 'index'),
    path('shop', views.shop, name='shop'),
    path('checkout', views.checkout, name = 'checkout'),
    path('contact', views.contact, name = 'contact'),
    path('cart', views.cart, name = 'cart'),
    path('details', views.details, name = 'details'),
    path('jeans', views.jeans, name = 'jeans'),
    path('shirts', views.shirts, name = 'shirts'),
    path('swimwear', views.swimwear, name = 'swimwear'),
    path('sleepwear', views.sleepwear, name = 'sleepwear'),
    path('sportswear', views.sportswear, name = 'sportswear'),
    path('jumpsuits', views.jumpsuits, name = 'jumpsuits'),
    path('blazers', views.blazers, name = 'blazers'),
    path('jackets', views.jackets, name = 'jackets'),
    path('shoes', views.shoes, name = 'shoes'),
    path('babies_dresses', views.babies_dresses, name = 'babies_dresses'),
    path('men_dresses', views.men_dresses, name = 'men_dresses'),
    path('women_dresses', views.women_dresses, name = 'women_dresses'),
    path('men_jeans', views.men_jeans, name = 'men_jeans'),
    path('search', views.search, name = 'search')
    #path('search/', Search.as_view(), name = 'search')



]
