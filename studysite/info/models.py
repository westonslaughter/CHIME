from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import image
# from imagekit.models import ImageSpecField
# from imagekit.processors import ResizeToFill


# Create your models here.
class ContactMod(models.Model):
        name= models.CharField(max_length=500)
        email= models.EmailField(max_length=500)
        comment= models.TextField()

        def __str__(self):
            return self.name

        # def get_absolute_url(self):
            # return reverse('thanks')

#### Models for the Meet the Team PAGE

# Create your models here.
class Org(models.Model):
    name = models.CharField(max_length=256)
    url = models.URLField()
    city = models.CharField(max_length=256)
    state = models.CharField(max_length=256)
    image = models.ImageField(upload_to='images/', max_length=100, default='NoPho.jpg')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("info:detail_view",kwargs={'pk':self.pk})

class Staff(models.Model):
    firstname = models.CharField(max_length=256)
    lastname = models.CharField(max_length=256)
    email = models.EmailField(max_length=256)
    title = models.CharField(max_length=256)
    org = models.ForeignKey(Org, related_name='employees', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', max_length=100, default='NoPho.jpg')
    # prof = ImageSpecField(source='image',
                                      # processors=[ResizeToFill(100, 50)],
                                      # format='JPEG',
                                      # options={'quality': 60})

    def __str__(self):
        return self.email

class Study(models.Model):
    studytitle = models.CharField(max_length=256)
    description = models.CharField(max_length=10000)
    studyimage = models.ImageField(upload_to='images/', max_length=100, default='NoPho.jpg')
    organisations = models.ForeignKey(Org,related_name="studies",on_delete=models.CASCADE)

    def __str__(self):
        return self.studytitle
