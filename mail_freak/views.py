from django.shortcuts import render
from django.views.generic import TemplateView
from .utils import send_mails


# Create your views here.

class SendMultipleMails(TemplateView):
    """
    Template View to send mails
    where multiple emails will set from templates
    """
    template_name = "send_mail.html"

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        email_sender = request.POST.get('formEmail', None)
        subject = request.POST.get('formSubject', None)
        main_text = request.POST.get('formMessage', None)
        recipient_list = request.POST.get('formRecipient', None)
        send_mails(email_sender, subject, main_text, recipient_list)
        print(recipient_list)

        return self.render_to_response(context)
