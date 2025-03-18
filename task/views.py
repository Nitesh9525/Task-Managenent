from rest_framework import generics
from .models import ProjectDetail, Developer, Task, TaskComment #,BugHistory, EnhancementHistory
from .serializers import ProjectDetailSerializer, DeveloperSerializer, TaskSerializer, TaskCommentSerializer,BugHistorySerializer, EnhancementHistorySerializer
from .filters import ProjectDetailFilter, DeveloperFilter, TaskFilter, TaskCommentFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class ProjectDetailListCreateView(generics.ListCreateAPIView):
    queryset = ProjectDetail.objects.all()
    serializer_class = ProjectDetailSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProjectDetailFilter
    search_fields = ["project_id",
                     "project_name",
                     "planned_start_date",
                     "planned_end_date"
                     ]  # Enables full-text search
    ordering_fields = '__all__'  # Allows ordering by any column


class ProjectDetailRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProjectDetail.objects.all()
    serializer_class = ProjectDetailSerializer
    


class DeveloperListCreateView(generics.ListCreateAPIView):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = DeveloperFilter
    search_fields = ['full_name', 'email', 'company']
    ordering_fields = '__all__'



class DeveloperRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer


class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = TaskFilter
    search_fields = ["developer_id",
                     "full_name",
                     "email",
                     "mobile_number",
                     "password_hash",
                     "created_at",
                     "company",
                     "monthly_rate",
                     "address",]
    ordering_fields = '__all__'


class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskCommentListCreateView(generics.ListCreateAPIView):
    queryset = TaskComment.objects.all()
    serializer_class = TaskCommentSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = TaskCommentFilter
    search_fields = ["STATUS_CHOICES",
                     "PRIORITY_CHOICES",
                     "task_id",
                     "developer",
                     "project",
                     "title",
                     "description",
                     "status",
                     "priority",
                     "due_date",
                     "planned_start_date",
                     "actual_start_date",
                     "actual_end_date",
                     "created_at",]
    ordering_fields = '__all__'


class TaskCommentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskComment.objects.all()
    serializer_class = TaskCommentSerializer


# class BugHistoryViewSet(viewsets.ModelViewSet):
#     queryset = BugHistory.objects.all()
#     serializer_class = BugHistorySerializer
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
#     filterset_fields = ['task', 'updated_by', 'project']
#     search_fields = ['bug_description']
#     ordering_fields = ['updated_at']

# class EnhancementHistoryViewSet(viewsets.ModelViewSet):
#     queryset = EnhancementHistory.objects.all()
#     serializer_class = EnhancementHistorySerializer
#     permission_classes = [IsAuthenticated]
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
#     filterset_fields = ['task', 'updated_by', 'project']
#     search_fields = ['enhancement_description']
#     ordering_fields = ['updated_at']

