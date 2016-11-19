from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^google66362829d50a6da0.html$', views.search_console_verification, name='search_console_verification'),
	url(r'^about/$', views.about, name='about'),
	url(r'^how-to/$', views.howto, name='how-to'),
	url(r'^contact/$', views.contact, name='contact'),
]
