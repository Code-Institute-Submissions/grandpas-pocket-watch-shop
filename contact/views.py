import os

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import ContactForm
from django.template.loader import render_to_string

def contact(request):
    if request.method == 'GET':
        contact_form = ContactForm()
    else:
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            email = contact_form.cleaned_data['email']
            message = contact_form.cleaned_data['message']
            try:
                subject = render_to_string(
                    'contact/confirmation_emails/confirmation_email_subject.txt')
                body = render_to_string(
                    'contact/confirmation_emails/confirmation_email_body.txt')

                send_mail(subject, body, email)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('contact_success')

    context = {
        'form': contact_form,
        'api_key': settings.GOOGLE_MAP_API_KEY,
    }

    return render(request, "contact/contact.html", context)


def contact_success(request):
    
    return render(request, "contact/contact_success.html")
