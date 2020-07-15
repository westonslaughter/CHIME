from django.conf.urls import url
from django.contrib import admin
from .views import (contactview)
app_name = 'info'

urlpatterns = [
     url(r'^$', contactview, name='info'),
]
