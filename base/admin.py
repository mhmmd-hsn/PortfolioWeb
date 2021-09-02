from django.contrib import admin
from .models import Project, Skill ,Message ,Tag

# Register your models here.

admin.site.register(Skill)
admin.site.register(Message)
admin.site.register(Project)
admin.site.register(Tag)