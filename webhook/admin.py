from django.contrib import admin

# Register your models here.
from webhook.models import WebHook


class WebHookAdmin(admin.ModelAdmin):
    list_display = (
        'event_name',
        'received_at',
        'event_id',
        'repository_name',
        'repository_owner_name',
        'repository_url',
        'sender_login',
    )


admin.site.register(WebHook, WebHookAdmin)
