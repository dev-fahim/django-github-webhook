from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json
from webhook.models import WebHook
from django.utils.timezone import now


@api_view(['POST'])
def get_webhook_events(request):
    body = request.body.decode('utf-8')
    WebHook.objects.add_record(request)
    print(now())
    print(body)
    return Response(data={'payloads': json.loads(request.body)}, status=status.HTTP_201_CREATED)
