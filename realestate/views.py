# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from website.models import MenuItem, SocialProfile
from .models import Property
from django.shortcuts import get_object_or_404

def detail_view(request, property_id):
    menu_items = MenuItem.objects.filter(active=True).order_by('position')
    social_profiles = SocialProfile.objects.filter(active=True).order_by('position')
    property = get_object_or_404(Property, pk = property_id)
    recent_properties = Property.objects.filter(active=True).order_by('-id')[:3]

    template = loader.get_template('realestate/property-detail.html')

    context = RequestContext(request, {
		'menu_items': menu_items,
		'social_profiles': social_profiles,
		'property': property,
        'recent_properties': recent_properties
	})
    return HttpResponse(template.render(context))
