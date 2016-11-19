from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from stdimage.models import StdImageField
from django.core.exceptions import ValidationError

class Property(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    address = models.CharField(max_length=255, verbose_name=_("Address"))
    neighborhood = models.CharField(max_length=255, verbose_name=_("Neighborhood"))
    city = models.CharField(max_length=254, blank=True, null=True, verbose_name=_("City"))
    state = models.CharField(max_length=254, blank=True, null=True, verbose_name=_("State"))
    country = models.CharField(max_length=254, blank=True, null=True, verbose_name=_("Country"))
    description = models.TextField(blank=True, null=True, verbose_name=_("Description"))
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name=_("Price"))
    latitude = models.FloatField(verbose_name=_("Latitude"))
    longitude = models.FloatField(verbose_name=_("Longitude"))
    map_zoom = models.PositiveIntegerField(verbose_name=_("Map Zoom"), default=16)
    active = models.BooleanField(verbose_name=_("Active"), default = True)

    def get_feature_picture(self):
        picture = self.pictures.filter(featured=True).first()
        return picture if not None else self.pictures.all().first()

    def __unicode__(self):
        return unicode(_("Property"))

    class Meta:
        verbose_name = _("Property")
        verbose_name_plural = _("Properties")

class PropertyPicture(models.Model):
    picture = StdImageField(upload_to="properties/main", blank=True, variations={
        'large': (1140, 630, True),
        'medium': (720, 400, True),
        'small': (767, 350, True),
        'thumbnail': (500, 500, True)
    }, verbose_name=_("Picture"))
    property = models.ForeignKey('Property', verbose_name=_("Property"),  related_name='pictures')
    featured = models.BooleanField(verbose_name=_("Featured"), default=False)

    def __unicode__(self):
        return unicode(_("Property Picture"))

    class Meta:
        verbose_name = _("Property Picture")
        verbose_name_plural = _("Property Pictures")
