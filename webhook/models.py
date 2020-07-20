from django.db import models
from uuid import uuid4

# Create your models here.


class WebHook(models.Model):
    event_id = models.UUIDField(editable=False, default=uuid4)
    event_name = models.CharField(max_length=255)
    payloads = models.TextField()
    received = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.event_name
