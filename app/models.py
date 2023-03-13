from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

PROVINCE_CHOICES=(
    ('PROVINCE 1','PROVINCE 1'),
    ('PROVINCE 2','PROVINCE 2'),
    ('PROVINCE 3','PROVINCE 3'),
    ('PROVINCE 4','PROVINCE 4'),
    ('PROVINCE 5','PROVINCE 5'),
    ('PROVINCE 6','PROVINCE 6'),
    ('PROVINCE 7','PROVINCE 7'),
)

class Customer(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    locality=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    zipcode=models.IntegerField()
    province=models.CharField(choices=PROVINCE_CHOICES,max_length=50)

    def __str__(self):
        return str(self.id)

CATEGORY_CHOICES=(
    ('M','Mobile'),
    ('L','Laptop'),
    ('TW','Top Wear'),
    ('BW','Bottom Wear'),
)

class Product(models.Model):
    title=models.CharField(max_length=100)
    selling_price=models.FloatField()
    discounted_price=models.IntegerField()
    description=models.TextField(blank=True)
    brand=models.CharField(max_length=100)
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    product_img=models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.id)
    

class Cart(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

STATUS_CHOICES=(
    ('ACCEPTED','ACCEPTED'),
    ('PACKED','PACKED'),
    ('ON THE WAY','ON THE WAY'),
    ('DELIVERED','DELIVERED'),
    ('CANCEL','CANCEL'),
)

class OrderPlaced(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    ordered_data=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=50,choices=STATUS_CHOICES,default='Pending')




    

