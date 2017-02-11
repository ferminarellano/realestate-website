from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^google66362829d50a6da0.html$', views.search_console_verification, name='search_console_verification'),
	url(_(r'^about/$'), views.about, name='about'),
	url(_(r'^how-to/$'), views.howto, name='how-to'),
	url(_(r'^blog/$'), views.blog, name='blog'),
	url(_(r'^blog/post/(?P<slug>[-\w\d\_]+)$'), views.blog_item, name='blog-detail-view'),
	url(_(r'^contact/$'), views.contact, name='contact'),
]
