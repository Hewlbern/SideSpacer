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
    #Memberships
    url(r'^memberships/' , include(("memberships.urls",'memberships'), namespace='memberships')),
    #Django Admin
    path('admin/', admin.site.urls),
    #User Management
    url(r'^accounts/', include('allauth.urls')),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
