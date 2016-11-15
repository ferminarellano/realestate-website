from django.contrib import admin
from realestate.models import Property
from modeltranslation.admin import TranslationAdmin

class PropertyAdmin(TranslationAdmin):
    group_fieldsets = True
    list_display = ('name', 'neighborhood', 'city', 'state', 'price', 'active')
    list_editable = ['price', 'active']

admin.site.register(Property, PropertyAdmin)
