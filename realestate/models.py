from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from stdimage.models import StdImageField

class Property(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    address = models.CharField(max_length=255, verbose_name=_("Address"))
    neighborhood = models.CharField(max_length=255, verbose_name=_("Neighborhood"))
    city = models.CharField(max_length=254, blank=True, null=True, verbose_name=_("City"))
    state = models.CharField(max_length=254, blank=True, null=True, verbose_name=_("State"))
    country = models.CharField(max_length=254, blank=True, null=True, verbose_name=_("Country"))
    description = models.TextField(blank=True, null=True, verbose_name=_("Description"))
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=_("Price"))
    picture = StdImageField(upload_to="properties/main", blank=True, variations={
        'large': (1050, 700, True),
        'thumbnail': (100, 100, True),
        'medium': (450, 300, True),
    }, verbose_name=_("Picture"))
    active = models.BooleanField(verbose_name=_("Active"), default = True)

    def __unicode__(self):
        return unicode(_("Property"))

    class Meta:
        verbose_name = _("Property")
        verbose_name_plural = _("Properties")
