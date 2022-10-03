from django.views.generic import TemplateView, ListView
from multiprocessing import context
from operator import contains
from django.shortcuts import render
from .models import*
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.

#Payment methods
p_method = PaymentMethods.objects.all()
#Address
address = Address.objects.all()
#Vendors
vendor = Vendor.objects.all()
#Lates arrival
latest = Latest.objects.all()
#Special collection
s_collection = SpecialCollection.objects.all()
#Carousel
carousel = Carousel.objects.all()
#Product
product = Product.objects.all()
#Cartegory
category = Category.objects.all()

# Home page
def index(request):
    context = {
            'product':product, 'category':category,
            'carousel': carousel, 's_collection':s_collection, 
            'latest': latest,'vendor':vendor,  
            'address':address,'pay_m':p_method
                }
    
    return render(request, 'eshopper/index.html', context)
    
#Shop page
def shop(request):
    context = {
            'product':product, 'pay_m':p_method,
            'address':address
                }
    return render(request, 'eshopper/shop.html', context)

#Checkout page
def checkout(request):
    context = {
            'pay_m':p_method, 'address':address
                }
    return render(request, 'eshopper/checkout.html', context)

#Contact page
def contact(request):
    context = {
            'pay_m':p_method, 'address':address
                }
    return render(request, 'eshopper/contact.html', context)

#Cart page
def cart(request):
    context = {
            'pay_m':p_method, 'address':address
                }
    return render(request, 'eshopper/cart.html',context)

# Product details page
def details(request):
    context = {
            'pay_m':p_method, 'product':product, 
            'address':address
                }
    return render(request, 'eshopper/detail.html', context)

# CATEGORIES
def babies_dresses(request):
    product = Product.objects.filter(babies_dress=True)

    context = {
            "pay_m":p_method, "product": product,
            'address':address, 'page_name': "Babies Dresses"
                }
    return render(request, 'eshopper/category.html', context)
                

def men_dresses(request):
    product = Product.objects.filter(men_dress=True)
    context = {
            "pay_m":p_method, "product": product,
            'address':address, 'page_name': "Men Dresses"
            }
    
    return render(request, 'eshopper/category.html', context)
    
def women_dresses(request):
    product = Product.objects.filter(women_dress=True)
    context = {
            "pay_m":p_method, "product": product, 
            'address':address, 'page_name': "Women Dresses"
            }
    
    return render(request, 'eshopper/category.html', context)

# Jeans
def jeans(request):
    product = Product.objects.filter(jeans=True)
    context =  {
            "pay_m":p_method, "product": product, 
            'address':address, 'page_name': "Jeans"
                }
    
    return render(request, 'eshopper/category.html', context)

# Shirts
def shirts(request):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
    product = Product.objects.filter(shirt=True)
    context = {
            "pay_m":p_method, "product": product, 
            'address':address, 'page_name': "Shirts"
                }
    return render(request, 'eshopper/category.html', context)

# Swimwear
def swimwear(request):
    product = Product.objects.filter(swimwear=True)

    context = {
            "pay_m":p_method, "product": product,
            'address':address, 'page_name': "Swimwear"
                }
    
    return render(request, 'eshopper/category.html', context)

# Sleepwear
def sleepwear(request):
    product = Product.objects.filter(sleepwear=True)
    context = {
            "pay_m":p_method, "product": product,
            'address':address, 'page_name': "Sleepwear"
                }
    
    return render(request, 'eshopper/category.html', context)

# sportswear
def sportswear(request):
    product = Product.objects.filter(sportwear=True)
    context = {
            "pay_m":p_method, "product": product,
            'address':address, 'page_name': "Sportswear"
                }
    
    return render(request, 'eshopper/category.html', context)

#jumpsuits
def jumpsuits(request):
    product = Product.objects.filter(jumpsuit=True)
    context = {
            "pay_m":p_method, "product": product,
            'address':address, 'page_name': "Jumpsuits"
                }
    
    return render(request, 'eshopper/category.html', context)

#blazers
def blazers(request):
    product = Product.objects.filter(blazer=True)
    context = {
            "pay_m":p_method, "product": product,
            'address':address, 'page_name': "Blazers"
                }
    
    return render(request, 'eshopper/category.html', context)

#jackets
def jackets(request):
    product = Product.objects.filter(jacket=True)
    context = {
            "pay_m":p_method, "product": product, 
            'address':address, 'page_name': "Jackets"
                }
    
    return render(request, 'eshopper/category.html', context)

#shoes
def shoes(request):
    product = Product.objects.filter(shoe=True)

    context =  {
            "pay_m":p_method, "product": product,
            'address':address, 'page_name': "Shoes"
                }
    
    return render(request, 'eshopper/category.html', context)

# Men Jeans
def men_jeans(request):
    product = Product.objects.filter(jeans=True, men_dress=True)
    context =  {
            "pay_m":p_method, "product": product, 
            'address':address, 'page_name': "Men Jeans"
                }

# Searching products
class Search(ListView):
    model = Product
    template_name = 'eshopper/category.html'
    def get_queryset(self):
        keyword= self.request.GET.get('keyword')
        product =  Product.objects.filter(name=keyword)
        context = {'page_name': " Search Results",
                 "pay_m":p_method,
                 "product": product,
                 'address':address
        }
        return context


def search(request):

    keyword= request.GET.get('keyword', '')
    if keyword:
        query_set = (
            Q(name_icontains_=keyword) | 
            Q(category_icontains_=keyword)
        )
    product = Product.objects.filter(query_set)
    context = {'page_name': " Search Results",
                 "pay_m":p_method,
                 "product": product,
                 'address':address
            }
    return render(request, 'eshopper/category.html', context)
 

