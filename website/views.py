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
from django.shortcuts import get_object_or_404
from django.utils import translation
from django.core.urlresolvers import reverse

from .models import MenuItem, SocialProfile, IntroBanner, Testimonial, BlogPost
from realestate.models import Property
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
	menu_items = MenuItem.objects.filter(active=True).order_by('position')
	social_profiles = SocialProfile.objects.filter(active=True).order_by('position')
	properties = Property.objects.filter(active=True).order_by('-featured','-id')
	banner_items = IntroBanner.objects.filter(active=True).order_by('position')

	template = 'website/index.html'

	context = {
		'menu_items': menu_items,
		'social_profiles': social_profiles,
		'properties': properties,
		'banner_items': banner_items,
		'request': request,
		'redirect_to': "/",
	}
	return render(request, template, context)

def about(request):
	menu_items = MenuItem.objects.filter(active=True).order_by('position')
	social_profiles = SocialProfile.objects.filter(active=True).order_by('position')
	testimonials = Testimonial.objects.filter(active=True).order_by('id')

	template = 'website/about.html'

	context = {
		'menu_items': menu_items,
		'social_profiles': social_profiles,
		'testimonials': testimonials,
		'request': request,
		'redirect_to': "/about/",
	}
	return render(request, template, context)

def howto(request):
	menu_items = MenuItem.objects.filter(active=True).order_by('position')
	social_profiles = SocialProfile.objects.filter(active=True).order_by('position')
	recent_properties = Property.objects.filter(active=True).order_by('-id')[:3]

	template = 'website/howto.html'

	context = {
		'menu_items': menu_items,
		'social_profiles': social_profiles,
		'properties': recent_properties,
		'request': request,
		'redirect_to': "/how-to/",
	}
	return render(request, template, context)

def blog(request):
	menu_items = MenuItem.objects.filter(active=True).order_by('position')
	social_profiles = SocialProfile.objects.filter(active=True).order_by('position')
	recent_properties = Property.objects.filter(active=True).order_by('-id')[:3]
	blog_items = BlogPost.objects.filter(active=True).order_by('date_published')
	paginator = Paginator(blog_items, 3)

	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	template = 'website/blog.html'

	context = {
		'menu_items': menu_items,
		'social_profiles': social_profiles,
		'properties': recent_properties,
		'posts': posts,
		'request': request,
		'redirect_to': "/blog/",
	}
	return render(request, template, context)

def blog_item(request, slug):
	menu_items = MenuItem.objects.filter(active=True).order_by('position')
	social_profiles = SocialProfile.objects.filter(active=True).order_by('position')
	recent_properties = Property.objects.filter(active=True).order_by('-id')[:3]
	blog_items = BlogPost.objects.filter(active=True).order_by('date_published')
	blog_post = get_object_or_404(BlogPost, slug = slug)
	template = 'website/blog-item.html'

	cur_language = translation.get_language()

	try:
		if cur_language == 'en':
			translation.activate('es')
			redirect_to = reverse('blog-detail-view', kwargs={'slug':blog_post.slug})
		if cur_language == 'es':
			translation.activate('en')
			redirect_to = reverse('blog-detail-view', kwargs={'slug':blog_post.slug})
	finally:
		translation.activate(cur_language)

	context = {
		'menu_items': menu_items,
		'social_profiles': social_profiles,
		'properties': recent_properties,
		'blog_post': blog_post,
		'request': request,
		'redirect_to': redirect_to,
	}
	return render(request, template, context)

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
		'message': message,
		'request': request,
		'redirect_to': "/contact/",
	}

	return render(request, template, context)

def search_console_verification(request):
	return HttpResponse("google-site-verification: google66362829d50a6da0.html")
