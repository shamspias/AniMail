from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class SendMultipleMails(TemplateView):
    """
    Template View to send mails
    where multiple emails will set from templates
    """
    template_name = "send_mail.html"

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        bar = self.request.POST['formEmail', None]
        print(bar)

        return self.render_to_response(context)
