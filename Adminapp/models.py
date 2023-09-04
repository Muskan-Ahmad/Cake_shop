from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=20)

    class Meta:
        db_table = "Category"

    def __str__(self):
        return self.category_name
class Product(models.Model):
    pname = models.CharField(max_length=20)
    price = models.FloatField(default=300)
    size = models.FloatField(default=0.5)
    desc = models.CharField(max_length=50)
    image = models.ImageField(default="abc.jpg",upload_to="images")
    cat = models.ForeignKey(to = "Category",on_delete=models.CASCADE)
    seller = models.CharField(max_length=50)



    class Meta:
        db_table = "Product"
    def __str__(self):
        return self.pname
    
class Userinfo(models.Model):
    username = models.CharField(max_length=20 ,primary_key=True)
    phn = models.CharField(max_length=10,default='9876543214')
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=20)
    add = models.CharField(max_length=100)
    class Meta:
        db_table = "Userinfo"
    def __str__(self):
        return self.username

class Paymentmaster(models.Model):
    cardno = models.CharField(max_length=20)
    cvv = models.CharField(max_length=4)
    expiry = models.CharField(max_length = 20)
    balance = models.FloatField(default = 1000)

    class Meta:
        db_table = "Paymentmaster"

class Query(models.Model):
    Name = models.CharField(max_length=30,primary_key=True)
    phn = models.CharField(max_length=10)
    email = models.EmailField()
    query = models.CharField(max_length=150)
    class Meta:
        db_table = 'Query'