from django.urls import path

from .views import SendMultipleMails

urlpatterns = [
    path('', SendMultipleMails.as_view(), name='send-multiple-mail'),
]
