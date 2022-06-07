from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class SendMultipleMails(TemplateView):
    """
    Template View to send mails
    where multiple emails will set from templates
    """
    template_name = "send_mail.html"

