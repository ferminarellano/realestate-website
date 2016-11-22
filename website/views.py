# -*- coding: utf-8 -*-
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, JsonResponse
from django.template import RequestContext, loader
from django.utils.translation import ugettext_lazy as _
import json
from django.core.mail import send_mail
from smtplib import SMTPException

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

		if len(errors) == 0:
			complete_message = 'Formulario de Contacto\nEnviado por: ' + name + '\nCorreo: '+ email + '\nAsunto: '+ subject + '\nMensaje: ' + message
			html = """
				<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
					<html xmlns="http://www.w3.org/1999/xhtml">
					    <head>
					        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
					        <title>""" + subject + """</title>
					        <style type="text/css">
					        body {margin: 0; padding: 0; min-width: 100%!important;}
					        .content {width: 100%; max-width: 600px;}
					        </style>
					    </head>
					    <body yahoo bgcolor="#f6f8f1">
							<div style="margin-bottom:10px;"><p>Hola, tienes un nuevo mensaje:</p></div>
							<div><b>Enviado por:</b> """ + name + """</div>
							<div><b>Correo:</b> """ + email + """</div>
							<div><b>Asunto:</b> """ + subject + """</div>
							<div><b>Mensaje:</b> """ + message + """</div>
					    </body>
					</html>
			"""
			try:
				mail_sent = send_mail(
				    subject,
				    complete_message,
				    'naturerichproperties@gmail.com',
				    ['mauricionegociosymas@yahoo.com'],
				    fail_silently=False,
					html_message=html
				)
				if mail_sent == 0:
					errors.append({
						"type" : "error",
						"field" : none,
						"message" : unicode(_("We encountered some problems trying to send your message. Please write us directly to: naturerichproperties@gmail.com")),
						"fields" : fields
					})
			except SMTPException:
				errors.append({
					"type" : "error",
					"field" : none,
					"message" : unicode(_("We encountered some problems trying to send your message. Please write us directly to: naturerichproperties@gmail.com")),
					"fields" : fields
				})

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
