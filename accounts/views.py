from django.shortcuts import render, redirect
import random
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from accounts.models import Profile
from twilio.rest import Client
from django.contrib import messages


def accounts(request):
    return render(request, 'accounts/login.html')


def generateOpt(request):
    if request.method == "POST":
        mobileno = request.POST.get('mobileno')
    # otp = ""
    # for _ in range(0, 4):
    #     otp += str(random.randint(0, 9))
    # account_sid = 'ACa679635a90ad2330e2c516ecf83318da'
    # auth_token = '46d791bf0c68f4ef29bb23f52afd7e2f'
    # client = Client(account_sid, auth_token)
    otp = "1234"
    user = User.objects.filter(username=mobileno)
    if not user:
        user = User(username=mobileno, password=otp)
    else:
        user = User.objects.get(username=mobileno)
        user.set_password(otp)
    user.save()

    # message = client.messages.create(
    #     body='Your Otp is ' + otp, to="+91" + mobileno, from_="+19852612254")

    return render(request, 'accounts/otp.html', {'mobileno': mobileno})


def otpverification(request):
    if request.method == "POST":
        mobileno = request.POST.get('mobileno')
        otp = request.POST.get('otp')
        user = authenticate(request, username=mobileno, password=otp)
        profile = Profile.objects.filter(user=user)
        if user is not None:
            login(request, user)
            if profile:
                pass
            else:
                profile = Profile(user=user)
                profile.save()
        else:
            messages.success(request, "Wrong OTP")
            return redirect('/accounts')
    print(mobileno, otp, "fdsafdsa")
    messages.success(request, "Logged In")
    return redirect('/')


def signout(request):
    logout(request)
    messages.success(request, "Logged Out")
    return redirect('/')
