from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from solo.admin import SingletonModelAdmin
from website.models import SiteConfiguration, MenuItem, SocialProfile, IntroBanner, Testimonial

class SiteConfigurationAdmin(SingletonModelAdmin, TranslationAdmin):
    group_fieldsets = True

class MenuItemAdmin(TranslationAdmin):
    group_fieldsets = True
    list_display = ('name', 'url', 'position', 'active')
    list_editable = ['position', 'active']

class SocialProfileAdmin(admin.ModelAdmin):
    list_display = ('social_profile', 'url', 'position', 'active')
    list_editable = ['active', 'position']

class IntroBannerAdmin(TranslationAdmin):
    group_fieldsets = True
    list_display = ('caption_title', 'position', 'active')
    list_editable = ['position', 'active']

class TestimonialAdmin(TranslationAdmin):
    group_fieldsets = True
    list_display = ('name', 'title', 'active')
    list_editable = ['active']

admin.site.register(SiteConfiguration, SiteConfigurationAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(SocialProfile, SocialProfileAdmin)
admin.site.register(IntroBanner, IntroBannerAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
