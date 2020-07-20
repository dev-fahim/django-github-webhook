from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json


@api_view(['POST'])
def get_webhook_events(request):
    body = request.body.decode('utf-8')
    print(request.headers.get('X-GitHub-Event'))
    print(json.loads(request.body))
    return Response(data={'payloads': json.loads(request.body)}, status=status.HTTP_201_CREATED)
