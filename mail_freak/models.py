from django.db import models

# Create your models here.

class Senders(models.Model):
    """
    List of all Senders
    """
    name = models.CharField(max_length=250, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name

class EmailTemplates(models.Model):
    """
    Basic Email send templates
    """
    name = models.CharField(max_length=20, blank=False, null=True)
    subject = models.TextField(black=True, null=True)
    main_text = models.TextField(blank=True, null=True)
    senders = models.ForeignKey(Senders, blank=True, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

