from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    task = models.TextField(max_length=255)
    details = models.TextField(null=True, blank=True)
    deadline = models.DateTimeField(null=True, blank=True)
    media = models.FileField(upload_to="../media_storage", null=True, blank=True)
    subtask_of = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    task_by = models.ForeignKey(User, related_name="task_by", on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)