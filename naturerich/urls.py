
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('website.urls')),
    url(r'^realestate/', include('realestate.urls')),
    url(r'^admin/', admin.site.urls),
]
