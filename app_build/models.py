from django.db import models

# Create your models here.
BUILD_STATUS_CHOICES = (
    ('Build started', 'Build started'),
    ('Build failed', 'Build failed'),
    ('Build finished', 'Build finished')
)


class AppBuildRecord(models.Model):

    build_on_event = models.CharField(max_length=255)
    build_started_at = models.DateTimeField(auto_now_add=True)
    build_status = models.CharField(max_length=255, choices=BUILD_STATUS_CHOICES)
    return_code = models.IntegerField()
    build_logs = models.TextField()

    def __str__(self):
        return self.build_on_event
