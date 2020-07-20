from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json
from webhook.models import WebHook
from django.utils.timezone import now


@api_view(['POST'])
def get_webhook_events(request):
    body = request.body.decode('utf-8')
    body_json = json.loads(body)
    WebHook.objects.create(
        event_name=request.headers.get('X-GitHub-Event'),
        payloads=body,
        repository_name=body_json['repository']['name'],
        repository_owner_name=body_json['repository']['owner']['name'],
        repository_url=body_json['repository']['url'],
    )
    print(now())
    print(body)
    return Response(data={'payloads': json.loads(request.body)}, status=status.HTTP_201_CREATED)
