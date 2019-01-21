from django.conf.urls import url

from Spaces import views

urlpatterns = [
url(r'^$', views.index, name='index'),
url(r'^pricing/$', views.pricing, name='pricing'),
url(r'^space/$', views.space, name='space'),
url(r'^submit/$', views.submit, name='submit'),
url(r'^contact/$', views.contact, name='contact'),
url(r'^add_category/$', views.add_category, name='add_category'),
url(r'^category/(?P<category_name_slug>[\w\-]+)/$',views.show_category, name='show_category'),
 url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
]
