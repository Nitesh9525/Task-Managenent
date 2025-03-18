import django_filters
from .models import ProjectDetail, Developer, Task, TaskComment


class ProjectDetailFilter(django_filters.FilterSet):
    project_name = django_filters.CharFilter(lookup_expr='icontains')  # Case-insensitive search
    planned_start_date = django_filters.DateTimeFilter(field_name="planned_start_date", lookup_expr="gte")
    planned_end_date = django_filters.DateTimeFilter(field_name="planned_end_date", lookup_expr="lte")

    class Meta:
        model = ProjectDetail
        fields = '__all__'  # Enables filtering on all columns


class DeveloperFilter(django_filters.FilterSet):
    full_name = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='icontains')
    company = django_filters.CharFilter(lookup_expr='icontains')
    created_at = django_filters.DateTimeFromToRangeFilter()  # Supports filtering by date range
    monthly_rate = django_filters.RangeFilter()  # Filters by minimum and maximum rate

    class Meta:
        model = Developer
        fields = '__all__'


class TaskFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    status = django_filters.MultipleChoiceFilter(choices=Task.STATUS_CHOICES)
    priority = django_filters.MultipleChoiceFilter(choices=Task.PRIORITY_CHOICES)
    due_date = django_filters.DateFromToRangeFilter()  # Supports filtering by date range
    planned_start_date = django_filters.DateTimeFromToRangeFilter()
    planned_end_date = django_filters.DateTimeFromToRangeFilter()

    class Meta:
        model = Task
        fields = '__all__'


class TaskCommentFilter(django_filters.FilterSet):
    comment_text = django_filters.CharFilter(lookup_expr='icontains')
    created_at = django_filters.DateTimeFilter(field_name="created_at", lookup_expr="gte")

    class Meta:
        model = TaskComment
        fields = '__all__'
