from django.urls import path
from . import views

urlpatterns = [
    path('icons', views.IIicons, name="ii-icon"),
    path('IIiconsPagination/', views.IIiconsPagination, name="ii-icon"),
    path('search/', views.IIiconsSearch, name="ii-search"),
]