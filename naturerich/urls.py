
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap

#     url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

urlpatterns = [
    url(r'^', include('website.urls')),
    url(r'^realestate/', include('realestate.urls')),
    url(r'^admin/', admin.site.urls),
]
