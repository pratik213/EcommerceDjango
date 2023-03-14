from django.shortcuts import render
from django.views import View
from . models import Customer,Product,Cart,OrderPlaced

# def home(request):
#  return render(request, 'app/home.html')

class ProductView(View):
    def get(self,request):
        topwears=Product.objects.filter(category='TW')
        bottomwears=Product.objects.filter(category='BW')
        mobile=Product.objects.filter(category='M')
        laptop=Product.objects.filter(category='L')
        return render(request,'app/home.html',
        {'topwears':topwears,'bottomwears':bottomwears,'mobile':mobile,'laptop':laptop})

    


# def product_detail(request):

#  return render(request, 'app/productdetail.html')

class ProductDetailView(View):
    def get(self,request,pk):
        product=Product.objects.get(pk=pk)
        return render(request,'app/productdetail.html',{'product':product})



def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request,data=None):
    if data==None:
        mobile=Product.objects.filter(category='M')
    elif data=='Redmi' or data=='Samsung':
        mobile=Product.objects.filter(category='M').filter(brand=data)
    elif data=='below':
        mobile=Product.objects.filter(category='M').filter(discounted_price__lt=10001)
    elif data=='above':
        mobile=Product.objects.filter(category='M').filter(discounted_price__gt=10000)

    return render(request, 'app/mobile.html',{'mobile':mobile})

def laptop(request,data=None):
    if data==None:
        laptop=Product.objects.filter(category='L')
    elif data=='Dell' or data=='Apple':
        laptop=Product.objects.filter(category='L').filter(brand=data)
    elif data=='below':
        laptop=Product.objects.filter(category='L').filter(discounted_price__lt=40001)
    elif data=='above':
        laptop=Product.objects.filter(category='L').filter(discounted_price__gt=40000)

    return render(request, 'app/laptop.html',{'laptop':laptop})

def topwear(request,data=None):
    if data==None:
        topwear=Product.objects.filter(category='TW')
    elif data=='adidas' or data=='nike':
        topwear=Product.objects.filter(category='TW').filter(brand=data)
    elif data=='below':
        topwear=Product.objects.filter(category='TW').filter(discounted_price__lt=5001)
    elif data=='above':
        topwear=Product.objects.filter(category='TW').filter(discounted_price__gt=5000)

    return render(request, 'app/topwear.html',{'topwear':topwear})

def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')
