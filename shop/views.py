from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Menu, Order, Timing
from accounts.models import Profile
import json
from django.contrib.auth.models import User
import datetime
from django.contrib import messages

# @login_required(login_url='/accounts')


def shop_open():
    now = datetime.datetime.now()
    timing = Timing.objects.get(id=1)
    if now.hour >= timing.shop_open.hour and now.hour <= timing.shop_close.hour and timing.open_now:
        print(timing.shop_open, timing.shop_close)
        return True
    else:
        return False


def home(request):
    if not shop_open():
        return redirect('/shopclose')
    menus = Menu.objects.filter(inStock=True).order_by('-pk')
    return render(request, 'shop/home.html', {'menus': menus})


def cart(request):
    if not shop_open():
        return redirect('/shopclose')
    menus = Menu.objects.filter(inStock=True).order_by('-pk')
    return render(request, 'shop/cart.html', {'menus': menus})


def profile(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        address = request.POST.get('address')
        profile = Profile.objects.get(
            user=User.objects.get(username=request.user))
        profile.user.first_name = firstname
        profile.user.last_name = lastname
        profile.address = address
        profile.user.save()
        profile.save()
        messages.success(request, "Saved ")
    profile = Profile.objects.get(user=User.objects.get(username=request.user))
    return render(request, 'shop/profile.html', {'profile': profile})


def shopclose(request):
    if shop_open():
        return redirect('/')
    return render(request, 'shop/shopclose.html')


@ login_required(login_url='/accounts')
def checkout(request):
    profile = Profile.objects.get(user=User.objects.get(username=request.user))
    return render(request, 'shop/checkout.html', {'profile': profile})


def placeorder(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        address = request.POST.get('address')
        cod = request.POST.get('cod')
        totalprice = request.POST.get('totalprice')
        cart = request.POST.get('cart')
        cart = json.loads(str(cart))
        #
        user = User.objects.get(username=request.user)
        user.first_name = firstname
        user.last_name = lastname
        user.save()
        #
        profile = Profile.objects.get(user=user)
        profile.address = address
        profile.save()
        for item in cart:
            order = Order(profile=profile, item=Menu.objects.get(
                id=item), quantity=cart[item])
            order.save()
            print(item, cart[item])
        print(firstname, lastname, address, totalprice, cod, cart)
    messages.success(request, "Order Placed")
    return redirect('/orders')


def orders(request):
    profile = Profile.objects.get(user=User.objects.get(username=request.user))
    orders_inprogress = Order.objects.filter(
        profile=profile, order_completed=False).order_by('-pk')
    completed_orders = Order.objects.filter(
        profile=profile, order_completed=True).order_by('-pk')
    return render(request, 'shop/orders.html', {'orders_inprogress': orders_inprogress, 'completed_orders': completed_orders})


def cancel(request, orderid):
    order = Order.objects.get(id=orderid)
    order.delete()
    return redirect('/orders')


def error_404(request, exception):
    return render(request, 'shop/404.html')
