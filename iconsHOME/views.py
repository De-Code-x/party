from django.shortcuts import render, redirect

# Create your views here.


def home(request):
    if not request.user.is_anonymous:
        return render(request, "home/base.html")
    return redirect('login-user')