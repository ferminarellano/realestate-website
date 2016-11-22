# -*- coding: utf-8 -*-
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, JsonResponse
from django.template import RequestContext, loader
from django.utils.translation import ugettext_lazy as _
import json
from django.core.mail import send_mail

from .models import MenuItem, SocialProfile, IntroBanner
from realestate.models import Property

def index(request):
	menu_items = MenuItem.objects.filter(active=True).order_by('position')
	social_profiles = SocialProfile.objects.filter(active=True).order_by('position')
	properties = Property.objects.filter(active=True).order_by('-id')
	banner_items = IntroBanner.objects.filter(active=True).order_by('position')

	template = loader.get_template('website/index.html')

	context = RequestContext(request, {
		'menu_items': menu_items,
		'social_profiles': social_profiles,
		'properties': properties,
		'banner_items': banner_items
	})
	return HttpResponse(template.render(context))

def about(request):
	menu_items = MenuItem.objects.filter(active=True).order_by('position')
	social_profiles = SocialProfile.objects.filter(active=True).order_by('position')

	template = loader.get_template('website/about.html')

	context = RequestContext(request, {
		'menu_items': menu_items,
		'social_profiles': social_profiles,
	})
	return HttpResponse(template.render(context))

def howto(request):
	menu_items = MenuItem.objects.filter(active=True).order_by('position')
	social_profiles = SocialProfile.objects.filter(active=True).order_by('position')

	template = loader.get_template('website/howto.html')

	context = RequestContext(request, {
		'menu_items': menu_items,
		'social_profiles': social_profiles,
	})
	return HttpResponse(template.render(context))

def contact(request):
	errors = []
	messages = []
	name = ""
	email = ""
	subject = ""
	message = ""

	if request.method == "POST":
		name = request.POST.get('name', '')
		email = request.POST.get('email', '')
		subject = request.POST.get('subject', '')
		message = request.POST.get('message', '')

		fields = {
			"name": name,
			"email": email,
			"subject": subject,
			"message": message
		}

		if len(name) == 0:
			errors.append({
				"type" : "error",
				"field" : "name",
				"message" : unicode(_("Please enter a valid name.")),
				"fields" : fields
			})

		if len(email) == 0:
			errors.append({
				"type" : "error",
				"field" : "email",
				"message" : unicode(_("Please enter a valid email.")),
				"fields" : fields
			})

		try:
			validate_email(email)
		except ValidationError as e:
			errors.append({
				"type" : "error",
				"field" : "email",
				"message" : unicode(_("Please enter a valid email.")),
				"fields" : fields
			})

		if len(subject) == 0:
			errors.append({
				"type" : "error",
				"field" : "subject",
				"message" : unicode(_("Please enter a valid subject.")),
				"fields" : fields
			})

		if len(message) == 0:
			errors.append({
				"type" : "error",
				"field" : "message",
				"message" : unicode(_("Please enter a valid message.")),
				"fields" : fields
			})

		complete_message = 'Formulario de Contact\nEnviado por: ' + name + '\nCorreo: '+ email + '\nAsunto: '+ subject + '\nMensaje: ' + message
		mail_sent = send_mail(
		    subject,
		    complete_message,
		    'naturerichproperties@gmail.com',
		    ['ferminarellano.hn@gmail.com'],
		    fail_silently=False,
		)

		if request.is_ajax():
			if len(errors) == 0:
				return HttpResponse(json.dumps([{
					"type" : "success",
					"message" : unicode(_("Your message was sent, we will contact you soon."))
				}]), content_type='application/json')
			else:
				data = json.dumps(errors)
				return HttpResponse(data, content_type='application/json')
		else:
			if len(errors) == 0:
				messages = [{
					"type" : "success",
					"message" : unicode(_("Your message was sent, we will contact you soon."))
				}]
				name = ""
				email = ""
				subject = ""
				message = ""
			else:
				messages = errors

	menu_items = MenuItem.objects.filter(active=True).order_by('position')
	social_profiles = SocialProfile.objects.filter(active=True).order_by('position')

	template = 'website/contact.html'

	context = {
		'menu_items': menu_items,
		'social_profiles': social_profiles,
		'messages': messages,
		'name': name,
		'email': email,
		'subject': subject,
		'message': message
	}

	return render(request, template, context)

def search_console_verification(request):
	return HttpResponse("google-site-verification: google66362829d50a6da0.html")
