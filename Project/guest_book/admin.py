from django.contrib import admin
from .models import Record

# Register your models here.
class RecordAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at', 'updated_at', 'status']
    list_filter = ['name', 'email']
    search_fields = ['name', 'text']
    fields = ['id', 'name', 'email', 'text', 'created_at', 'updated_at', 'status']
    readonly_fields = ['created_at', 'updated_at', 'id']

admin.site.register(Record, RecordAdmin)