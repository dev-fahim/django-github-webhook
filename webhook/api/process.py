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


def process_build(payloads, event_name):
    returned = -1
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
    try:
        obj.save()
        project_dir = '/home/fahim' + '/app/' + project_dir
        os.chdir(os.path.expanduser(project_dir))
        # /home/fahim/app/dev-fahim/django-github-webhook/build.sh
        os.system("git pull origin master")
        docker = subprocess.run(
            "docker-compose down;"
            "docker-compose build;"
            "docker-compose up -d;"
            "docker-compose logs --tail=100;",
            shell=True, capture_output=True
        )

        error_logs = docker.stderr.decode('utf-8')
        print("Now on: " + os.getcwd())
        logs = docker.stdout.decode('utf-8')
        returned = docker.returncode
        print(returned)
        if returned > 0:
            obj.build_status = BUILD_STATUS_CHOICES[1][0]
            obj.build_logs = error_logs
        else:
            obj.build_status = BUILD_STATUS_CHOICES[2][0]
            obj.build_logs = logs
        obj.return_code = returned
        obj.save()
        os.chdir(working_directory)
    except:
        obj.build_status = BUILD_STATUS_CHOICES[1][0]
        obj.build_logs = sys.stderr
        obj.return_code = returned
        obj.save()
        pprint.pprint("error occurred on running file...")
