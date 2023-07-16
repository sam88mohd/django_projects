from django.db import models

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)


class User(models.Model):
    first_name = models.CharField(null=False, max_length=30, default='john')
    last_name = models.CharField(null=False, max_length=30, default='doe')


class Instructor(User):
    pass
