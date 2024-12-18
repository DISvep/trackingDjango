from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    description = models.TextField()
    image = models.ImageField(upload_to="task_image/", blank=True, null=True)
    media = models.FileField(upload_to="task_media/", blank=True, null=True)
    status = models.CharField(max_length=12, choices=[
        ('_in_progress', 'In Progress'), ("_done", "Done"), ('_expired', "Expired")
    ])
    priority = models.CharField(max_length=7, choices=[
        ("_low", "Low"), ("_mid", "Middle"), ("_high", "High")
    ])
    deadline = models.DateTimeField()


class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='post_likes')
    dislikes = models.ManyToManyField(User, related_name='post_dislikes')
    image = models.ImageField(upload_to="comment_image/", blank=True, null=True)
    media = models.FileField(upload_to='comment_media/', blank=True, null=True)
