from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from solo.admin import SingletonModelAdmin
from website.models import SiteConfiguration, MenuItem, SocialProfile

class SiteConfigurationAdmin(SingletonModelAdmin, TranslationAdmin):
    group_fieldsets = True

class MenuItemAdmin(TranslationAdmin):
    group_fieldsets = True
    list_display = ('name', 'url', 'position', 'active')
    list_editable = ['position', 'active']

class SocialProfileAdmin(admin.ModelAdmin):
    list_display = ('social_profile', 'url', 'position', 'active')
    list_editable = ['active', 'position']

admin.site.register(SiteConfiguration, SiteConfigurationAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(SocialProfile, SocialProfileAdmin)
