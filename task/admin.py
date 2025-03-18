from django.contrib import admin
from .models import ProjectDetail, Developer, Task, TaskComment, BugHistory, EnhancementHistory

# Register your models here.

class ProjectDetailAdmin(admin.ModelAdmin):
    list_display = ('project_id', 'project_name', 'planned_start_date', 'planned_end_date')
    search_fields = ('project_name',)
    list_filter = ('planned_start_date', 'planned_end_date')

class DeveloperAdmin(admin.ModelAdmin):
    list_display = ('developer_id', 'full_name', 'email', 'created_at', 'company')
    search_fields = ('full_name', 'email')
    list_filter = ('created_at',)

# class TaskAdmin(admin.ModelAdmin):
#     list_display = ('task_id', 'title', 'developer', 'project', 'status', 'priority', 'due_date')
#     search_fields = ('title', 'developer__full_name', 'project__project_name')
#     list_filter = ('status', 'priority', 'due_date')


class TaskAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = (
        'task_id', 
        'title', 
        'developer_id', 
        'project_id', 
        'status', 
        'priority', 
        'due_date', 
        'created_at', 
        'delayed_start_by_days', 
        'delayed_end_by_days', 
        'total_number_of_day_taken'
    )

    # Fields to filter by in the right sidebar
    list_filter = ('status', 'priority')

    # Fields to search by
    search_fields = ('title', 'description')

    # Fields that are read-only (computed fields)
    readonly_fields = (
        'delayed_start_by_days', 
        'delayed_end_by_days', 
        'total_number_of_day_taken'
    )

    # Optional: Customize the display of computed fields
    def delayed_start_by_days(self, obj):
        return obj.delayed_start_by_days or "N/A"

    def delayed_end_by_days(self, obj):
        return obj.delayed_end_by_days or "N/A"

    def total_number_of_day_taken(self, obj):
        return obj.total_number_of_day_taken or "N/A"

    # Add column headers for computed fields
    delayed_start_by_days.short_description = 'Delayed Start (Days)'
    delayed_end_by_days.short_description = 'Delayed End (Days)'
    total_number_of_day_taken.short_description = 'Total Days Taken'


class TaskCommentAdmin(admin.ModelAdmin):
    list_display = ('comment_id', 'task', 'developer', 'project', 'created_at')
    search_fields = ('task__title', 'developer__full_name')
    list_filter = ('created_at',)


from django.contrib import admin
from .models import BugHistory, EnhancementHistory

class BugHistoryAdmin(admin.ModelAdmin):
    list_display = ('bug_history_id', 'task', 'updated_by', 'project', 'updated_at')
    list_filter = ('task', 'updated_by', 'project')  # Add filters in the admin list view
    search_fields = ('bug_description',)  # Add search functionality

class EnhancementHistoryAdmin(admin.ModelAdmin):
    list_display = ('enhancement_history_id', 'task', 'updated_by', 'project', 'updated_at')
    list_filter = ('task', 'updated_by', 'project')  # Add filters in the admin list view
    search_fields = ('enhancement_description',)  # Add search functionality

# Registering models with the admin site
admin.site.register(ProjectDetail, ProjectDetailAdmin)
admin.site.register(Developer, DeveloperAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(TaskComment, TaskCommentAdmin)
admin.site.register(BugHistory, BugHistoryAdmin)
admin.site.register(EnhancementHistory, EnhancementHistoryAdmin)



