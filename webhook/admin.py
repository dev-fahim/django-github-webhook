from django.contrib import admin

# Register your models here.
from webhook.models import WebHook

admin.site.register(WebHook)
