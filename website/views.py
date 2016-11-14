# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import MenuItem, SocialProfile

def index(request):
	menu_items = MenuItem.objects.filter(active=True).order_by('position')
	social_profiles = SocialProfile.objects.filter(active=True).order_by('position')
	template = loader.get_template('website/index.html')
	context = RequestContext(request, {
		'menu_items': menu_items,
		'social_profiles': social_profiles
	})
	return HttpResponse(template.render(context))
