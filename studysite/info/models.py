from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class ContactMod(models.Model):
        name= models.CharField(max_length=500)
        email= models.EmailField(max_length=500)
        comment= models.TextField()

        def __str__(self):
            return self.name

        # def get_absolute_url(self):
            # return reverse('thanks')
