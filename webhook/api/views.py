from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json
from webhook.models import WebHook
from django.utils.timezone import now
import subprocess
import os
from rest_framework.generics import ListAPIView
from rest_framework import permissions
from webhook.api.serializers import WebHookSerializer
import pprint
from app_build.models import AppBuildRecord, BUILD_STATUS_CHOICES
import sys
import time
from django_q.tasks import async_task

@api_view(['POST'])
def get_webhook_events(request):
    payloads = request.data
    WebHook.objects.add_record(request)
    event_name = str(request.headers.get('X-GitHub-Event'))
    if event_name in ['push', "None"]:
        async_task('webhook.api.process.process_build', payloads, event_name)
    return Response(data={'payloads': payloads}, status=status.HTTP_201_CREATED)


class WebHookListAPIView(ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]
    serializer_class = WebHookSerializer

    def get_queryset(self):
        return WebHook.objects.all().order_by('-id')
