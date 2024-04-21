from django.db import models

# Create your models here.

from django.db import models


class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=100)
    creation_time = models.DateTimeField()
    author = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='language_logos/')
    detailed_information = models.TextField()

    def __str__(self):
        return self.name


class PythonFramework(models.Model):
    name = models.CharField(max_length=100)
    creation_time = models.DateTimeField()
    author = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='framework_logos/')
    detailed_information = models.TextField()

    def __str__(self):
        return self.name


class PythonLibrary(models.Model):
    name = models.CharField(max_length=100)
    creation_time = models.DateTimeField()
    author = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='library_logos/')
    detailed_information = models.TextField()

    def __str__(self):
        return self.name


class PythonTopic(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
