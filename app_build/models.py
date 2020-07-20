from django.db import models

# Create your models here.


class AppBuildRecord(models.Model):
    BUILD_STATUS_CHOICES = (
        ('Build started', 'Build started'),
        ('Build failed', 'Build failed'),
        ('Build finished', 'Build finished')
    )

    build_by = models.CharField(max_length=255)
    build_started_at = models.DateTimeField(auto_now_add=True)
    build_status = models.CharField(max_length=255)
    return_code = models.PositiveSmallIntegerField()
    build_logs = models.TextField()
