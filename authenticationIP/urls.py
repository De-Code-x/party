from django.urls import path
from . import views

urlpatterns = [
    path('login-user/', views.login_required, name="login-user"),
    path('logout-user/', views.logout_me, name="login-out"),
    path('login-verify/', views.login_verification, name="login-verify"),
]