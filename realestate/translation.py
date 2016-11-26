from modeltranslation.translator import translator, TranslationOptions
from realestate.models import Property, PropertyPicture

class PropertyTranslationOptions(TranslationOptions):
    fields = ('name', 'address', 'description')

class PropertyPictureTranslationOptions(TranslationOptions):
    fields = ('alt_text',)

translator.register(Property, PropertyTranslationOptions)
translator.register(PropertyPicture, PropertyPictureTranslationOptions)
