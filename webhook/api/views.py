from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json


@api_view(['POST'])
def get_webhook_events(request):
    body = request.body.decode('utf-8')
    print(body)
    return Response(data={'payloads': body}, status=status.HTTP_201_CREATED)
