from django.shortcuts import render,redirect
from django.views import View
from . models import Customer,Product,Cart,OrderPlaced
from . forms import CustomerRegistrationForm,LoginForm,CustomerProfileForm
from django.contrib import messages
from django.contrib.auth import login,authenticate
from django.db.models import Q
from django.http import JsonResponse


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
    user=request.user
    product_id=request.GET.get('prod_id')
    product=Product.objects.get(id=product_id)
    Cart(user=user,product=product).save()
    return redirect('/cart')

def show_cart(request):
    if request.user.is_authenticated:
        user=request.user
        cart=Cart.objects.filter(user=user)
        amount=0.00
        shipping_amount=70.0
        total_amount=0.0
        cart_product=[p for p in Cart.objects.all() if p.user==user]
        if cart_product:
            for p in cart_product:
                tempamount=(p.quantity * p.product.discounted_price)
                amount+=tempamount
                total_amount=amount+shipping_amount
            # import pdb;pdb.set_trace()
            return render(request,'app/addtocart.html',{'carts':cart,'total_amount':total_amount,'amount':amount})
        else:
            return render(request,'app/emptycart.html')

def plus_cart(request):
    if request.method=='GET':
        prod_id=request.GET['prod_id']
        c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        amount=0.0
        shipping_amount=70.0
        cart_product=[p for p in Cart.objects.all() if p.user==request.user]
        for p in cart_product:
            tempamount=(p.quantity * p.product.discounted_price)
            amount+=tempamount
            total_amount=amount+shipping_amount
        
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':total_amount
            }
        # import pdb;pdb.set_trace()
        return JsonResponse(data)




def buy_now(request):
 return render(request, 'app/buynow.html')

# def profile(request):
#  return render(request, 'app/profile.html')

class ProfileView(View):
    def get(self,request):
        form=CustomerProfileForm()
        return render(request,"app/profile.html",{'form':form,'active':'btn-primary'})

    def post(self,request):
        form=CustomerProfileForm(request.POST)
        if form.is_valid():
            usr=request.user
            name=form.cleaned_data['name']
            locality=form.cleaned_data['locality']
            city=form.cleaned_data['city']
            zipcode=form.cleaned_data['zipcode']
            province=form.cleaned_data['province']
            reg=Customer(user=usr,name=name,locality=locality,city=city,zipcode=zipcode,province=province)
            reg.save()
            messages.success(request, "Congratulation!! Profile Updated Successfully")
            form=CustomerProfileForm()
        return render(request, "app/profile.html",{'form':form,'active':'btn-primary'})

def address(request):
    add=Customer.objects.filter(user=request.user)
    return render(request, 'app/address.html',{'add':add,'active':'btn-primary'})

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
    elif data=='puma' or data=='sonam':
        topwear=Product.objects.filter(category='TW').filter(brand=data)
    elif data=='below':
        topwear=Product.objects.filter(category='TW').filter(discounted_price__lt=5001)
    elif data=='above':
        topwear=Product.objects.filter(category='TW').filter(discounted_price__gt=5000)

    return render(request, 'app/topwear.html',{'topwear':topwear})

def bottomwear(request,data=None):
    if data==None:
        bottomwear=Product.objects.filter(category='BW')
    elif data=='adidas' or data=='nike':
        bottomwear=Product.objects.filter(category='BW').filter(brand=data)
    elif data=='below':
        bottomwear=Product.objects.filter(category='BW').filter(discounted_price__lt=5001)
    elif data=='above':
        bottomwear=Product.objects.filter(category='BW').filter(discounted_price__gt=5000)

    return render(request, 'app/bottomwear.html',{'bottomwear':bottomwear})
class CustomerRegistration(View):
    def get(self,request):
        form=CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html',{'form':form})

    def post(self,request):
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, "Congratulation you have completed your registration")
            form.save()
        return render(request, 'app/customerregistration.html',{'form':form})


def checkout(request):
 return render(request, 'app/checkout.html')
