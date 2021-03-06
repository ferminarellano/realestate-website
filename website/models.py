from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from solo.models import SingletonModel
from stdimage.models import StdImageField
from django.utils.text import slugify
from django.core.urlresolvers import reverse

class SiteConfiguration(SingletonModel):
    sitename = models.CharField(verbose_name=_("Site name"), max_length=255, default="Site Name")
    site_url = models.CharField(verbose_name=_("Site URL"), max_length=255)
    telephone = models.CharField(verbose_name=_("Mobile"), max_length=255)
    telephone2 = models.CharField(verbose_name=_("Landline"), max_length=255)
    email = models.EmailField(verbose_name=_("Email"))
    address1 = models.CharField(verbose_name=_("Address Line 1"), max_length=255)
    address2 = models.CharField(verbose_name=_("Address Line 2"), max_length=255)
    about = models.TextField(verbose_name=_("About"), blank=True, null=True)

    def __unicode__(self):
        return unicode(_("Site Configuration"))

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

class SocialProfile(models.Model):
    options = (
        ('facebook', 'Facebook'),
        ('twitter', 'Twitter'),
        ('linkedin', 'LinkedIn'),
        ('google-plus', 'Google+'),
    )
    social_profile = models.CharField(choices=options, verbose_name=_("Social Profile"),max_length=20, default='facebook', unique=True)
    url = models.URLField(verbose_name=_("Social Profile URL"))
    position = models.PositiveIntegerField(verbose_name=_("Position"), unique=True)
    active = models.BooleanField(verbose_name=_("Active"), default = True)

    def __unicode__(self):
        return unicode(_("Social Profile"))

    class Meta:
        verbose_name = _("Social Profile")
        verbose_name_plural = _("Social Profiles")

class IntroBanner(models.Model):
    picture = StdImageField(upload_to="banner", blank=True, variations={
        'large': (1903, 450, True),
    }, verbose_name=_("Picture"))
    caption_title = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("Caption Title"))
    caption_description = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("Caption Description"))
    position = models.PositiveIntegerField(verbose_name=_("Position"), unique=True)
    offset = models.IntegerField(verbose_name=_("Offset"), blank=True, null=True)
    active = models.BooleanField(verbose_name=_("Active"), default = True)

    def __unicode__(self):
        return unicode(_("Banner Item"))

    class Meta:
        verbose_name = _("Banner Item")
        verbose_name_plural = _("Banner Items")

class Testimonial(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    picture = StdImageField(upload_to="testimonials", blank=True, variations={
        'thumbnail': (200, 200, True),
    }, verbose_name=_("Picture"))
    text = models.TextField(verbose_name=_("Testimonial text"))
    active = models.BooleanField(verbose_name=_("Active"), default = True)

    def __unicode__(self):
        return unicode(_("Testimonial"))

    class Meta:
        verbose_name = _("Testimonial")
        verbose_name_plural = _("Testimonials")

class BlogPost(models.Model):
    title = models.CharField(verbose_name=_("Title"), max_length=255)
    content = models.TextField(verbose_name=_("Content"), blank=True, null=True)
    intro = models.TextField(verbose_name=_("Introduction"), blank=True, null=True)
    picture = StdImageField(upload_to="blog_pics", blank=True, variations={
        'thumbnail': (200, 200, True),
    }, verbose_name=_("Picture"))
    date_published = models.DateField(verbose_name=_("Date Published"))
    slug = models.SlugField(max_length=255, blank=True, null=True)
    active = models.BooleanField(verbose_name=_("Active"), default = True)

    def get_absolute_url(self):
        return reverse('blog-detail-view', args=(self.slug,))

    def save(self):
        self.slug = slugify(self.title)
        super(BlogPost, self).save()
