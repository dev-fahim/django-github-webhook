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


def process_build(payloads, event_name):
    returned = -1
    k = "Hello"
    logs = None
    error_logs = None

    working_directory = os.getcwd()
    project_dir = payloads['repository']['full_name']
    obj = AppBuildRecord.objects.create(
        repository_name=payloads['repository']['name'],
        repository_owner_name=payloads['repository']['owner']['login'],
        build_on_event=event_name.title(),
        build_status=BUILD_STATUS_CHOICES[0][0],
        return_code=returned,
        build_logs="Not available"
    )
    k = "Added"
    obj.save()
    k = "Saved"
    project_dir = '/home/fahim' + '/app/' + project_dir
    os.chdir(os.path.expanduser(project_dir))
    # /home/fahim/app/dev-fahim/django-github-webhook/build.sh
    os.system("git pull origin master")

    shell_run = subprocess.run([working_directory + '/build.sh'], capture_output=True, shell=True)

    error_logs = shell_run.stderr.decode('utf-8')
    print("Now on: " + os.getcwd())
    logs = shell_run.stdout.decode('utf-8')
    returned = shell_run.returncode
    if returned > 0:
        obj.build_status = BUILD_STATUS_CHOICES[1][0]
        obj.build_logs = error_logs
    else:
        obj.build_status = BUILD_STATUS_CHOICES[2][0]
        obj.build_logs = logs
    obj.return_code = returned
    obj.save()
    os.chdir(working_directory)
    k = "Done try"
    return k


@api_view(['POST'])
def get_webhook_events(request):
    payloads = request.data
    WebHook.objects.add_record(request)
    event_name = str(request.headers.get('X-GitHub-Event'))
    k = None
    if event_name in ['push']:
        k = process_build(payloads, event_name)
    print(k)
    return Response(data={'payloads': payloads}, status=status.HTTP_201_CREATED)


class WebHookListAPIView(ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]
    serializer_class = WebHookSerializer

    def get_queryset(self):
        return WebHook.objects.all().order_by('-id')
