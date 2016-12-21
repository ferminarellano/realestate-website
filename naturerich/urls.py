
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import ugettext_lazy as _
from realestate.sitemap import ListingsSitemap
from website.sitemap import WebsiteSitemap

sitemaps = {
    'properties' : ListingsSitemap,
    'static' : WebsiteSitemap,
}

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

urlpatterns += i18n_patterns(
    url(r'^', include('website.urls')),
    url(r'^', include('realestate.urls')),
    prefix_default_language=False
)
