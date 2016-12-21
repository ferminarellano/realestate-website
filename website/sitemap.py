from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class WebsiteSitemap(Sitemap):
    i18n = True

    def items(self):
        return ['index', 'about', 'how-to', 'contact', 'list-view']

    def location(self, item):
        return reverse(item)
