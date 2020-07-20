from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json
from webhook.models import WebHook
from django.utils.timezone import now
import subprocess
import os


def process_build(payloads):
    working_directory = os.getcwd()
    project_dir = payloads['repository']['full_name']
    os.chdir('~/app/' + project_dir)
    shell_run = subprocess.run(['source', working_directory + 'build.sh'], capture_output=True)
    error_logs = shell_run.stderr.decode('utf-8')
    logs = shell_run.stdout.decode('utf-8')
    returned = shell_run.returncode
    print(now())
    print(error_logs)
    print(logs)
    print(returned)
    os.chdir(working_directory)


@api_view(['POST'])
def get_webhook_events(request):
    WebHook.objects.add_record(request)
    payloads = json.loads(request.body)
    process_build(payloads)
    return Response(data={'payloads': payloads}, status=status.HTTP_201_CREATED)
