from modeltranslation.translator import translator, TranslationOptions
from website.models import SiteConfiguration, MenuItem

class SiteConfigurationTranslationOptions(TranslationOptions):
    fields = ('sitename', 'address1', 'address2', 'about')

class MenuItemTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(SiteConfiguration, SiteConfigurationTranslationOptions)
translator.register(MenuItem, MenuItemTranslationOptions)
