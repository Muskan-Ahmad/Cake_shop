from django.contrib import admin
from . models import Category,Product,Paymentmaster

class Category_admin(admin.ModelAdmin):
    list_display = ("category_name",)

class Product_admin(admin.ModelAdmin):
    list_display = ("pname","price","desc","size","image","cat")
class Payment_master_admin(admin.ModelAdmin):
    list_display = ("cardno","cvv","expiry","balance")

admin.site.register(Category,Category_admin)
admin.site.register(Product,Product_admin)
admin.site.register(Paymentmaster,Payment_master_admin)

# Register your models here.
