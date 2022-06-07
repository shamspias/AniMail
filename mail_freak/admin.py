from django.contrib import admin
from .models import Senders, EmailTemplates

admin.site.register(Senders)
admin.site.register(EmailTemplates)