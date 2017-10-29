from django.db import models

class Skills(models.Model):
    PERCENT_CHOICES = [
        ( 1, '0%' ),   
        ( 25, '25%' ),   
        ( 50, '50%' ),   
        ( 75, '75%' ),   
        ( 100, '100%' ),   
    ]
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    perc = models.IntegerField(choices=PERCENT_CHOICES)

    def __str__(self):
        return self.name

