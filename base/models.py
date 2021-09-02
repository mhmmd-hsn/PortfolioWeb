from django.db import models
import uuid
from django.db.models.fields import TextField
# Create your models here.


class Skill(models.Model):
    title = models.CharField(max_length=200)
    percent = models.IntegerField(null=True,blank=True)
    def __str__(self):
        return self.title

class Message(models.Model):
    Name = models.CharField(max_length=200, null=True)
    Email = models.CharField(max_length=200, null=True)
    Subject = models.CharField(max_length=200, null=True)
    Message = models.TextField()
    
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,  unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name

class Tag(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    thumbnail = models.ImageField(null=True)
    Github = models.CharField(max_length=300 , null =True)
    tags = models.ManyToManyField(Tag)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,  unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title

