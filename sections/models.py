from django.db import models
from django.conf import settings

class Experience(models.Model):

    PERC_CHOICES = [
        (1, '0%'), 
        (10, '10%'),
        (20, '20%'),
        (25, '25%'), 
        (30, '30%'),
        (40, '40%'),
        (50, '50%'), 
        (60, '60%'),
        (70, '70%'),
        (75, '75%'), 
        (80, '80%'),
        (90, '90%'),
        (100, '100%'), 
    ]

    name = models.CharField(max_length=100)
    level = models.CharField(max_length=100, blank=True)
    perc = models.IntegerField(choices=PERC_CHOICES)

    def __str__(self):
        return self.name

class Work(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    url = models.CharField(max_length=2000, blank=True)
    github = models.CharField(max_length=2000,blank=True)

    def __str__(self):
        return self.name

class Work_Image(models.Model):
    work = models.ForeignKey(Work, on_delete=models.CASCADE)
    file = models.ImageField(upload_to='portfolio')

    def __str__(self):
        return self.work.name

    def path(self):
        return settings.MEDIA_ROOT + self.file.name

class Content(models.Model):
    name = models.SlugField(unique=True, max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.name
