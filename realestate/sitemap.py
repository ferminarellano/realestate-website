from django.contrib.sitemaps import Sitemap
from .models import Property

class ListingsSitemap(Sitemap):
    i18n = True

    def items(self):
        return Property.objects.filter(active=True)
