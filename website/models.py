from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from solo.models import SingletonModel

class SiteConfiguration(SingletonModel):
    sitename = models.CharField(verbose_name=_("Site name"), max_length=255, default="Site Name")
    site_url = models.CharField(verbose_name=_("Site URL"), max_length=255)
    telephone = models.CharField(verbose_name=_("Telephone"), max_length=255)
    email = models.EmailField(verbose_name=_("Email"))
    address1 = models.CharField(verbose_name=_("Address Line 1"), max_length=255)
    address2 = models.CharField(verbose_name=_("Address Line 2"), max_length=255)
    about = models.TextField(verbose_name=_("About"), blank=True, null=True)

    def __unicode__(self):
        return _("Site Configuration")

    class Meta:
        verbose_name = _("Site Configuration")

class MenuItem(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=255)
    url = models.CharField(verbose_name=_("URL"), max_length=255)
    position = models.PositiveIntegerField(verbose_name=_("Position"), unique=True)
    active = models.BooleanField(verbose_name=_("Active"), default = True)

    def __unicode__(self):
        return unicode(_("Menu Item"))

    class Meta:
        verbose_name = _("Menu Item")
        verbose_name_plural = _("Menu items")

#class SocialProfiles(models.Model):
