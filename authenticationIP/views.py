from django.shortcuts import render,HttpResponse, redirect
from .models import DecodeXCred as auth2
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages

# Create your views here.

def login_required(request):
    return render(request, 'auth/login.html')

def logout_me(request):
    logout(request)
    # Display a notification
    messages.success(request, "Logged Out Successfully!")
    return redirect('login-user')

def login_verification(request):
    if request.method == 'POST':
        username = request.POST.get('DecodeX-user')
        passwd = request.POST.get('DecodeX-pwd')
        sID = request.POST.get('DecodeX-sID')

        user = authenticate(request, username=username, password=passwd)
        final_user = auth2(user, DecodeXID=sID)

        if final_user is not None:
            login(request, user)
            messages.success(request, "Logging in Success!!")
            return redirect("home")
        else:
            messages.warning(request, "Logging in Failed!!")
            return render(request, 'auth/login.html')


        print(request.POST.get('username'))
    return HttpResponse("Page Not Found")