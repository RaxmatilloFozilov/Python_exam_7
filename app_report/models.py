from django.db import models

# Create your models here.


class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=100)
    creation_time = models.DateTimeField()
    author = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='media/language_logos/')
    detailed_information = models.TextField()

    def __str__(self):
        return self.name


class PythonFramework(models.Model):
    name = models.CharField(max_length=100)
    creation_time = models.DateTimeField()
    author = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='media/framework_logos/',default='')
    detailed_information = models.TextField()

    def __str__(self):
        return self.name


class PythonLibrary(models.Model):
    name = models.CharField(max_length=100)
    detailed_information = models.TextField()

    def __str__(self):
        return self.name


class PythonTopic(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


