
from django.contrib import admin
from django.utils.html import format_html
from .models import (
    ProjectDetail, Developer, Task, TaskComment, 
    BugHistory, EnhancementHistory, ProjectFile
)

# Project File Inline (for multiple file uploads under ProjectDetail)
class ProjectFileInline(admin.TabularInline):
    model = ProjectFile
    extra = 1  # Allows adding one or more files at a time
    fields = ["file", "uploaded_at"]
    readonly_fields = ["uploaded_at"]

# ProjectDetail Admin with inline file uploads
class ProjectDetailAdmin(admin.ModelAdmin):
    list_display = ('project_id', 'project_name', 'planned_start_date', 'planned_end_date')
    search_fields = ('project_name',)
    list_filter = ('planned_start_date', 'planned_end_date')
    inlines = [ProjectFileInline]  # Attach files inline under each project

# Developer Admin
class DeveloperAdmin(admin.ModelAdmin):
    list_display = ('developer_id', 'full_name', 'email', 'created_at', 'company')
    search_fields = ('full_name', 'email')
    list_filter = ('created_at',)

# Task Admin
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'task_id', 'title', 'developer_id', 'project_id', 'status', 
        'priority', 'due_date', 'created_at', 
        'delayed_start_by_days', 'delayed_end_by_days', 'total_number_of_day_taken'
    )
    list_filter = ('status', 'priority')
    search_fields = ('title', 'description')
    readonly_fields = ('delayed_start_by_days', 'delayed_end_by_days', 'total_number_of_day_taken')

    def delayed_start_by_days(self, obj):
        return obj.delayed_start_by_days or "N/A"

    def delayed_end_by_days(self, obj):
        return obj.delayed_end_by_days or "N/A"

    def total_number_of_day_taken(self, obj):
        return obj.total_number_of_day_taken or "N/A"

    delayed_start_by_days.short_description = 'Delayed Start (Days)'
    delayed_end_by_days.short_description = 'Delayed End (Days)'
    total_number_of_day_taken.short_description = 'Total Days Taken'

# Task Comment Admin
class TaskCommentAdmin(admin.ModelAdmin):
    list_display = ('comment_id', 'task', 'developer', 'project', 'created_at')
    search_fields = ('task__title', 'developer__full_name')
    list_filter = ('created_at',)

# Bug History Admin
class BugHistoryAdmin(admin.ModelAdmin):
    list_display = ('bug_history_id', 'task', 'updated_by', 'project', 'updated_at')
    list_filter = ('task', 'updated_by', 'project')
    search_fields = ('bug_description',)

# Enhancement History Admin
class EnhancementHistoryAdmin(admin.ModelAdmin):
    list_display = ('enhancement_history_id', 'task', 'updated_by', 'project', 'updated_at')
    list_filter = ('task', 'updated_by', 'project')
    search_fields = ('enhancement_description',)

# Project File Admin with File Preview
@admin.register(ProjectFile)
class ProjectFileAdmin(admin.ModelAdmin):
    list_display = ('file_id', 'project', 'file_preview', 'uploaded_at')
    search_fields = ('project__project_name', 'file')
    list_filter = ('uploaded_at',)

    def file_preview(self, obj):
        """Display a link to download the file"""
        return format_html('<a href="{}" target="_blank">Download</a>', obj.file.url) if obj.file else "No file"

    file_preview.short_description = "File"

# Registering models with the admin site
admin.site.register(ProjectDetail, ProjectDetailAdmin)
admin.site.register(Developer, DeveloperAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(TaskComment, TaskCommentAdmin)
admin.site.register(BugHistory, BugHistoryAdmin)
admin.site.register(EnhancementHistory, EnhancementHistoryAdmin)
