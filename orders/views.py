from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Toppings, RegularPizza, ScicilianPizza, Salads, DinnerPlate, Subs, Pasta, Order
import json
# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})
    context = {
    "toppings":Toppings.objects.all(),
    "salads":Salads.objects.all(),
    "regularPizza":RegularPizza.objects.all(),
    "scicilianPizza":ScicilianPizza.objects.all(),
    "dinnerplaters":DinnerPlate.objects.all(),
    "subs":Subs.objects.all(),
    "pasta":Pasta.objects.all()
    }
    return render(request,"orders/menu.html", context)
def loginn(request):
    if request.method == "GET":
        return render(request,"orders/login.html")
    else:
        username = request.POST["uname"]
        password = request.POST["psw"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:
                context = {
                "orders":Order.objects.all(),
                }
                return render(request, "orders/vieworders.html", context)
            else:
                return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "orders/login.html", {"message": "Invalid credentials."})
def register(request):
    if request.method == "GET":
        return render(request,"orders/register.html")
    else :
        username = request.POST["uname"]
        password = request.POST["psw"]
        email = request.POST["email"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            return render(request, "orders/register.html", {"message": "username or email address already in use"})
        user = User.objects.create_user(username, email, password)
        # Update fields and then save again
        user.first_name = request.POST["fname"]
        user.last_name = request.POST["lname"]
        user.save()
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
def logoutt(request):
    logout(request)
    return render(request, "orders/login.html", {"message": "Logged out."})
def makeorder(request):
    context = {
    "toppings":Toppings.objects.all(),
    "salads":Salads.objects.all(),
    "regularPizza":RegularPizza.objects.all(),
    "scicilianPizza":ScicilianPizza.objects.all(),
    "dinnerplaters":DinnerPlate.objects.all(),
    "subs":Subs.objects.all(),
    "pasta":Pasta.objects.all()
    }
    return render(request, "orders/shopingCart.html", context)
def confirmorder(request):
    orders = []
    order = json.loads(request.POST["order"])
    for orde in order['items']:
        orders.append(json.loads(orde))
    context = {
    "firstname": request.user.first_name,
    "items":orders,
    "price":order['price'],
    "total":order['total']
    }
    return render(request, "orders/confirmorder.html", context)
def confirmedorder(request):
    orders = []
    order = json.loads(request.POST["order"])
    for orde in order['items']:
        orders.append(json.loads(orde))
    confirmedorder = Order.objects.create(firstname=request.user.first_name,items=request.POST["order"],price=order['price'],totalprice=order['total'])
    confirmedorder.save()
    return render(request, "orders/payment.html")
