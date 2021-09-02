from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomeView , name='HomeView'),
    path('about/',views.AboutMe , name='AboutMe'),
    path('contact/',views.ContactView , name='contact'),
    path('projects/',views.ProjectView , name='projects'),

]