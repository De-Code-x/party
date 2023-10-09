from django.urls import path
from . import views

urlpatterns = [
    path('icons', views.BSicons, name="bs-icon"),
    path('BSiconsPagination/', views.BSiconsPagination, name="bs-icon"),
    path('search/', views.BSiconsSearch, name="bs-search"),
]