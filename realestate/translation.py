from modeltranslation.translator import translator, TranslationOptions
from realestate.models import Property

class PropertyTranslationOptions(TranslationOptions):
    fields = ('name', 'address', 'description')

translator.register(Property, PropertyTranslationOptions)
