from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^detail/(?P<property_id>[0-9]+)$', views.detail_view, name='detail-view'),
	url(r'^properties/$', views.list_view, name='list-view'),
]
