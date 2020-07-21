from django.db import models
from uuid import uuid4

# Create your models here.
BUILD_STATUS_CHOICES = (
    ('Build started', 'Build started'),
    ('Build failed', 'Build failed'),
    ('Build finished', 'Build finished')
)


class AppBuildRecord(models.Model):
    build_id = models.UUIDField(editable=False, default=uuid4, verbose_name='Build local ID')
    event_id = models.UUIDField(editable=False, default=uuid4, verbose_name='Event local ID')
    build_on_event = models.CharField(max_length=255)
    repository_name = models.CharField(max_length=255)  # ['repository']['name']
    repository_owner_name = models.CharField(max_length=255)  # ['repository']['owner']['login']
    build_started_at = models.DateTimeField(auto_now_add=True)
    build_status = models.CharField(max_length=255, choices=BUILD_STATUS_CHOICES)
    return_code = models.IntegerField()
    build_logs = models.TextField()

    def __str__(self):
        return self.build_on_event
