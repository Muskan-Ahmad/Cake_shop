from django.db import models
from Adminapp.models import Userinfo,Product
from datetime import datetime


class Mycart(models.Model):
    user = models.ForeignKey(to='Adminapp.Userinfo',on_delete=models.CASCADE)
    cake = models.ForeignKey(to='Adminapp.Product',on_delete=models.CASCADE)
    qty = models.IntegerField()
    class Meta:
        db_table = "Mycart"

class ordermaster(models.Model):
    user = models.ForeignKey(to= "Adminapp.Userinfo",on_delete=models.CASCADE)
    amount = models.FloatField(default=1000)
    dateoforder = models.DateTimeField(default=datetime.now())
    details = models.CharField(max_length=1000,default='Null')

    class Meta:
        db_table = "ordermaster"