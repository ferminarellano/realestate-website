from django.contrib import admin
from realestate.models import Property, PropertyPicture
from modeltranslation.admin import TranslationAdmin
from django.forms.models import BaseInlineFormSet
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class PropertyPictureInlineFormSet(BaseInlineFormSet):
   def clean(self):
      super(PropertyPictureInlineFormSet, self).clean()
      total = 0
      for form in self.forms:
         if not form.is_valid():
            return
         if form.cleaned_data and not form.cleaned_data.get('DELETE'):
             is_featured = form.cleaned_data['featured']
             if is_featured:
                 total += 1

      if total > 1:
         raise ValidationError(_('There can only be one featured picture in a property'))

class PropertyPictureInline(admin.TabularInline):
    model = PropertyPicture
    formset = PropertyPictureInlineFormSet
    extra = 1

class PropertyAdmin(TranslationAdmin):
    group_fieldsets = True
    list_display = ('name', 'neighborhood', 'city', 'state', 'price', 'active')
    list_editable = ['price', 'active']
    inlines = [
        PropertyPictureInline,
    ]


admin.site.register(Property, PropertyAdmin)
