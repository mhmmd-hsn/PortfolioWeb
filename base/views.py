from django.shortcuts import render
from django.shortcuts import render,redirect
from .models import Skill , Project ,Tag ,Message
from .forms import MessageForm
from django.contrib import messages
# Create your views here.

def HomeView(request):
    skills = Skill.objects.all()
    projects = Project.objects.all()
    tags = Tag.objects.all()
    skills = Skill.objects.all()
    
    context = {'skills':skills , 'projects':projects ,'tags':tags} 
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


def message_view(request):
    messages = Message.objects.all()
    context = {'messages':messages}
    return render(request,'base/message.html',context)
