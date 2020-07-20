from rest_framework import serializers
from webhook.models import WebHook
import json


class WebHookSerializer(serializers.ModelSerializer):

    class Meta:
        model = WebHook
        exclude = ('payloads', )
