from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _

from . import views

urlpatterns = [
	url(_(r'^realestate/detail/(?P<slug>[-\w\d\_]+)$'), views.detail_view, name='detail-view'),
	url(_(r'^realestate/properties/$'), views.list_view, name='list-view'),
]
