"""
URL configuration for IconPort project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from authenticationIP import urls as auth
from iconsHOME import urls as HURLS
from bootstrapIcons import urls as BSURLS
from ionIcons import urls as IIURLS

urlpatterns = [
    path('admin/', admin.site.urls),
    path('decodex-person-verification/', include(auth)),
    path('', include(HURLS)),
    path('bootstrap-icons/', include(BSURLS)),
    path('ion-icons-v2/', include(IIURLS)),
]
