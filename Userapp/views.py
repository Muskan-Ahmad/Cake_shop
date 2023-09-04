from django.shortcuts import render,redirect
from Adminapp.models import Category,Product,Userinfo,Paymentmaster,Query
from .models import Mycart,ordermaster
from django.contrib import messages

# Create your views here.
def homepage(request):
    cat = Category.objects.all()
    cake = Product.objects.all()
    store = Product.objects.all()
    return render(request,"homepage.html",{"cats":cat,"cakes":cake,"stores" : store})
def login(request):
    cat = Category.objects.all()
    store = Product.objects.all()
    if request.method == 'GET':
        return render(request,"login.html",{"cats":cat,"stores":store})
    else:
        uname = request.POST["uname"]
        pwd  = request.POST["pwd"]
        try:
            Userinfo.objects.get(username = uname,password = pwd)
        except:
            messages.success(request,"invalid username or password")
            return redirect(login)
        else:
            request.session["uname"] = uname
            messages.success(request,'Login Successful')
            return redirect(homepage)
def showcake(request,id):
    cat = Category.objects.all()
    id = Category.objects.get(id = id)
    cake = Product.objects.filter(cat = id)
    store = Product.objects.all()
    return render(request,"homepage.html",{"cakes":cake,"cats" : cat,"stores" :store})
def signup(request):
    cat = Category.objects.all()
    cake = Product.objects.all()
    store = Product.objects.all()
    if request.method == 'GET':
        return render(request,"signup.html",{"cats" : cat,"cakes":cake,"stores":store})
    else:
        uname = request.POST["uname"]
        email = request.POST["email"]
        phn = request.POST['phn']
        pwd = request.POST["pwd"]
        u1 = Userinfo(uname,email,pwd,phn)
        u1.save()
        return redirect(homepage)

def viewdetails(request,id):
    cat = Category.objects.all()
    cake = Product.objects.get(id = id)
    store = Product.objects.all()
    return render(request,"viewdetails.html",{"cats":cat,"cake":cake,"stores":store})
        
def logout(request):
    request.session.clear()
    return redirect(homepage)
def addtocart(request):
    if request.method == 'POST':
        if "uname" in request.session:
            user = request.session['uname']
            cakeid = request.POST['cakeid']
            qty = request.POST['qty']
            cake = Product.objects.get(id = cakeid)
            user = Userinfo.objects.get(username = user)
            try:
                Mycart.objects.get(user = user,cake = cake)
            except:
                cart = Mycart()
                cart.user = user
                cart.cake = cake
                cart.qty = qty
                cart.save()
                messages.success(request,"item added to cart")
                return redirect(homepage)
            else:
                messages.success(request,'item already exist in cart')
                return redirect(homepage)
           
        else:
            return redirect(login)
def cart(request):
    cat = Category.objects.all()
    store = Product.objects.all()
    uname = request.session['uname']
    user = Userinfo.objects.get(username = uname)
    if request.method == 'GET':
        
        items = Mycart.objects.filter(user = user)
        total = 0
        for item in items:
            total += item.qty*item.cake.price
        request.session['total'] = total
        return render(request,"cart.html",{"items" : items,"cats":cat,"stores":store})
    else:
        id = request.POST['cakeid']
        qty = request.POST['qty']
        cake = Product.objects.get(id = id)
        item = Mycart.objects.get(user = user,cake = cake)
        item.qty = qty
        item.save()
        return redirect(cart)
def home(request):
        return render(request,'home.html',{})
def removeitem(request):
    uname = request.session['uname']
    user = Userinfo.objects.get(username = uname)
    id = request.POST['cakeid']
    cake = Product.objects.get(id = id)
    item = Mycart.objects.get(user = user,cake=cake)
    item.delete()
    return redirect(cart)

def makepayment(request,id):
   
    if request.method == "GET":
        if id != 0:
            user = request.session['uname']
            try:
                item = Mycart.objects.get(user = user , cake = id)
            except:
                return render(request,"makepayment.html",{})
            else:
                order = 'single'
                return render(request,"makepayment.html",{"orders" : order,"items" : item})        
    else:
        accno = request.POST["accno"]
        cvv = request.POST["cvv"]
        expiry = request.POST["expiry"]
        seller = Paymentmaster.objects.get(cardno = "333",cvv = "333",expiry = "09/2024")
        try:
            buyer = Paymentmaster.objects.get(cardno = accno ,cvv = cvv,expiry = expiry)
        except:
            return redirect(signup)
        else:
            uname = request.session['uname']
            user = Userinfo.objects.get(username = uname)
            if id == 0:
                buyer.balance -= request.session['total']
                seller.balance += request.session['total']
                buyer.save()
                seller.save()
                amount = request.session['total']
                details = ''
                items = Mycart.objects.filter(user=user)
                for item in items :
                    details += item.cake.pname+ " "
                    item.delete()
                order = ordermaster()
                order.user = user
                order.amount = amount
                order.details = details
                order.save()    
            else:
    
                item = Mycart.objects.get(user = user , cake = id)
                single = item.qty*item.cake.price
                buyer.balance -= item.qty*item.cake.price
                seller.balance += item.qty*item.cake.price
                buyer.save()
                seller.save()
                amount = item.qty*item.cake.price
                order = ordermaster()
                order.user = user
                order.amount = amount
                order.details = item.cake
                order.save()
                item.delete()

            
        return redirect(cart)
def myprofile(request):
    cat = Category.objects.all()
    store = Product.objects.all()
    uname = request.session["uname"]
    user = Userinfo.objects.get(username = uname)
        
    return render(request,"profile.html",{"user":user,"cats":cat,"stores":store})

def myorders(request):
    uname = request.session['uname']
    user = Userinfo.objects.get(username = uname)
    cat = Category.objects.all()
    store = Product.objects.all()
    if request.method == 'GET':
        
        item = ordermaster.objects.filter(user = user)
        return render(request,"myorder.html",{"items":item,"cats":cat,"stores":store})
    else:
        action = request.POST["action"]
        id = request.POST["cakeid"]
        item = ordermaster.objects.get(user = user,id = id)
        item.delete()
        return redirect(myorders)
    return redirect(homepage)


    
def contact(request):
    cat = Category.objects.all()
    store = Product.objects.all()
    if request.method == 'GET':
        return render(request,'contact.html',{"cats":cat,"stores":store})
    else:
        qname = request.POST['qname']
        qphn = request.POST['qphn']
        qmail = request.POST['qmail']
        query = request.POST['query']
        que = Query(qname,qphn,qmail,query)
        que.save()
        messages.success(request,'sent successful')
        return redirect(homepage)
    
def wishlist(request):
    return redirect(homepage)