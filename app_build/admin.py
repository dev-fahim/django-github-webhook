from django.contrib import admin

# Register your models here.
from app_build.models import AppBuildRecord


class AppBuildRecordAdmin(admin.ModelAdmin):

    list_display = [
        'build_on_event',
        'build_started_at',
        'build_status',
        'return_code'
    ]


admin.site.register(AppBuildRecord, AppBuildRecordAdmin)
