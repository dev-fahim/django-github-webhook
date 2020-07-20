from django.db import models
from uuid import uuid4
import json

# Create your models here.


class WebHookManager(models.Manager):

    @staticmethod
    def add_record(request):
        body = json.dumps(request.data)
        body_json = request.data
        WebHook.objects.create(
            event_name=str(request.headers.get('X-GitHub-Event')).title(),
            payloads=body,
            repository_name=body_json['repository']['name'],
            repository_owner_name=body_json['repository']['owner']['login'],
            repository_url=body_json['repository']['url'],
            sender_login=body_json['sender']['login'],
        )


class WebHook(models.Model):
    event_id = models.UUIDField(editable=False, default=uuid4, verbose_name='Event local ID')
    repository_name = models.CharField(max_length=255)  # ['repository']['name']
    repository_owner_name = models.CharField(max_length=255)  # ['repository']['owner']['login']
    repository_url = models.URLField()  # ['repository']['url']
    sender_login = models.CharField(max_length=255, verbose_name='Event by')  # ['sender']['login']
    event_name = models.CharField(max_length=255)
    payloads = models.TextField()
    received_at = models.DateTimeField(auto_now_add=True)

    objects = WebHookManager()

    def __str__(self):
        return self.event_name
