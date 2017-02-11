from modeltranslation.translator import translator, TranslationOptions
from website.models import SiteConfiguration, MenuItem, IntroBanner, Testimonial, BlogPost

class SiteConfigurationTranslationOptions(TranslationOptions):
    fields = ('sitename', 'address1', 'address2', 'about')

class MenuItemTranslationOptions(TranslationOptions):
    fields = ('name', 'url')

class IntroBannerTranslationOptions(TranslationOptions):
    fields = ('caption_title', 'caption_description')

class TestimonialTranslationOptions(TranslationOptions):
    fields = ('title', 'text')

class BlogPostTranslationOptions(TranslationOptions):
    fields = ('title','content', 'intro', 'slug')

translator.register(SiteConfiguration, SiteConfigurationTranslationOptions)
translator.register(MenuItem, MenuItemTranslationOptions)
translator.register(IntroBanner, IntroBannerTranslationOptions)
translator.register(Testimonial, TestimonialTranslationOptions)
translator.register(BlogPost, BlogPostTranslationOptions)
