from django.contrib import admin

from . models import(
    Customer,
    Product,
    Cart,
    OrderPlaced
)

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=['id','user','name','locality','city','zipcode','province']

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    # pass
    list_display=['id','title','selling_price','description','discounted_price','brand','category','product_img']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display=['id','user','product','quantity']

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    pass
    list_display=['id','user','customer','product','ordered_data','quantity','status']
