from django.shortcuts import render
from django.shortcuts import render,redirect
from .models import Skill , Project 
from .forms import MessageForm
from django.contrib import messages
# Create your views here.

def HomeView(request):
    skills = Skill.objects.all()
    projects = Project.objects.all()
    
    context = {'skills':skills , 'projects':projects } 
    return render(request, 'base/home.html', context)


def AboutMe(request):

    context = {}
    return render(request,'base/about.html',context)


def ContactView (request):
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            
    form = MessageForm()
    context = {'form': form}
    return render(request,'base/contact.html', context)

def ProjectView(request):
    projects = Project.objects.all()
    context = {'projects':projects}
    return render(request,'base/projects.html',context)
