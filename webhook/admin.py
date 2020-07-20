from django.contrib import admin

# Register your models here.
from webhook.models import WebHook


class WebHookAdmin(admin.ModelAdmin):
    list_display = (
        'event_name',
        'event_id',
        'received'
    )


admin.site.register(WebHook, WebHookAdmin)
