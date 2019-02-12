"""Space URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static

from Spaces import views
from submitaspace import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #Spaces
    url(r'^Spaces/', include(('Spaces.urls', 'Spaces'), namespace='Spaces')),
    #Submitting a Space
    url(r'^submitaspace/', include(('submitaspace.urls', 'submitaspace'), namespace='submitaspace')),
    #Product
    url(r'^products/', include(('product.urls', 'products'), namespace='products')),
    #Carts
    url(r'^cart/' , include(("carts.urls",'carts'), namespace='cart')),
    #Django Admin
    path('admin/', admin.site.urls),
    #User Management
    url(r'^accounts/', include('allauth.urls')),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
