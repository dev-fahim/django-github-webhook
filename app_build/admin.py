from django.contrib import admin

# Register your models here.
from app_build.models import AppBuildRecord


class AppBuildRecordAdmin(admin.ModelAdmin):

    list_display = [
        'build_on_event',
        'build_id',
        'event_id',
        'repository_name',
        'repository_owner_name',
        'build_started_at',
        'build_status',
        'return_code'
    ]
    readonly_fields = ('build_logs', )
    list_filter = [
        'build_status',
    ]
    search_fields = ['build_id', 'event_id']


admin.site.register(AppBuildRecord, AppBuildRecordAdmin)
