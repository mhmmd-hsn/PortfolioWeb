from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls import url

from django.conf import settings
import os
from django.views.static import serve 
from django.urls import re_path


urlpatterns = [
    path('',views.HomeView , name='HomeView'),
    path('about/',views.AboutMe , name='AboutMe'),
    path('contact/',views.ContactView , name='contact'),
    path('projects/',views.ProjectView , name='projects'),
    path('renegadeone/',views.message_view , name='messages'), 
    # re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    # re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]

