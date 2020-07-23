from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from .views import (contactview)
from info import views



app_name = 'info'

urlpatterns = [
     path('stafflist/',views.OrgListView.as_view(),name='stafflist'),
     url(r'^$', contactview, name='info'),
     path('stafflist/<int:pk>/',views.StaffDetailView.as_view(),name='detail_view')

]
