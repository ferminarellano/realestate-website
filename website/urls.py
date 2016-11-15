from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^about/$', views.about, name='about'),
	url(r'^how-to/$', views.howto, name='how-to'),
	url(r'^contact/$', views.contact, name='contact'),
]
