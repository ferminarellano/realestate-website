from modeltranslation.translator import translator, TranslationOptions
from website.models import SiteConfiguration, MenuItem, IntroBanner

class SiteConfigurationTranslationOptions(TranslationOptions):
    fields = ('sitename', 'address1', 'address2', 'about')

class MenuItemTranslationOptions(TranslationOptions):
    fields = ('name',)

class IntroBannerTranslationOptions(TranslationOptions):
    fields = ('caption_title', 'caption_description')

translator.register(SiteConfiguration, SiteConfigurationTranslationOptions)
translator.register(MenuItem, MenuItemTranslationOptions)
translator.register(IntroBanner, IntroBannerTranslationOptions)
