from django.db import models


# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    status = models.CharField(max_length=12, choices=[
        ('_in_progress', 'In Progress'), ("_done", "Done"), ('_expired', "Expired")
    ])
    priority = models.CharField(max_length=7, choices=[
        ("_low", "Low"), ("_mid", "Middle"), ("_high", "High")
    ])
    deadline = models.DateTimeField()
