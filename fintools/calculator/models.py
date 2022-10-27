from django.db import models
from django.core.validators import validate_email

# Create your models here.
class MailingMember(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, validators=[validate_email])

    def __str__(self):
        return self.name
