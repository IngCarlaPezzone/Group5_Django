from django.db import models

# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=200)

class Member(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    github = models.CharField(max_length=200, null=True)
    role = models.CharField(max_length=200, null=True)
    skills = models.ManyToManyField(Skill)
