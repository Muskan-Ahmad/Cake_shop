from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage),
    path("login",views.login),
    path('showcake/<id>',views.showcake),
    path('signup',views.signup),
    path('viewdetails/<id>',views.viewdetails),
    path('logout',views.logout),
    path('addtocart',views.addtocart),
    path('cart',views.cart),
    path('makepayment/<id>',views.makepayment),
    path('myprofile',views.myprofile),
    path('myorder',views.myorders),
    path('removeitem',views.removeitem),
    path('contact/',views.contact),

]