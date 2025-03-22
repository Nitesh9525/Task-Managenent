from rest_framework import generics
from .models import ProjectDetail, Developer, Task, TaskComment ,BugHistory, EnhancementHistory, ProjectFile #, Image, File
from .serializers import ProjectDetailSerializer, DeveloperSerializer, TaskSerializer, TaskCommentSerializer ,BugHistorySerializer, EnhancementHistorySerializer,ProjectFileSerializer, MultipleProjectFileUploadSerializer #,DeveloperWithProjectsSerializer
from .filters import ProjectDetailFilter, DeveloperFilter, TaskFilter, TaskCommentFilter, EnhancementHistoryFilter , BugHistoryFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework import status  # ✅ Import status




class ProjectDetailListCreateView(generics.ListCreateAPIView):
    queryset = ProjectDetail.objects.all()
    serializer_class = ProjectDetailSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProjectDetailFilter
    search_fields = ["project_id",
                     "project_name",
                     "planned_start_date",
                     "planned_end_date",
                     "developers",
                     ]  # Enables full-text search
    ordering_fields = '__all__'  # Allows ordering by any column


class ProjectDetailRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProjectDetail.objects.all()
    serializer_class = ProjectDetailSerializer
    


class DeveloperListCreateView(generics.ListCreateAPIView):
    queryset = Developer.objects.all()
    # serializer_class = DeveloperSerializer
    serializer_class = DeveloperSerializer #DeveloperWithProjectsSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = DeveloperFilter
    search_fields = ['full_name', 'email', 'company']
    ordering_fields = '__all__'



class DeveloperRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer #DeveloperWithProjectsSerializer


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
# BugHistory List and Create API
class BugHistoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = BugHistory.objects.all()
    serializer_class = BugHistorySerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = BugHistoryFilter  # Use the BugHistoryFilter class
    ordering_fields = '__all__'  # Fields to order by
    search_fields = ["bug_history_id",
                     "task",
                     "updated_by",
                     "project",
                     "bug_description",
                     "updated_at",]  # Fields to search by

# BugHistory Retrieve, Update, Destroy API
class BugHistoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BugHistory.objects.all()
    serializer_class = BugHistorySerializer
 
# EnhancementHistory List and Create API
class EnhancementHistoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = EnhancementHistory.objects.all()
    serializer_class = EnhancementHistorySerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_class = EnhancementHistoryFilter  # Use the EnhancementHistoryFilter class
    ordering_fields = '__all__' # Fields to order by
    search_fields = ["enhancement_history_id",
                     "task",
                     "updated_by",
                     "project",
                     "enhancement_description",
                     "updated_at",]  # Fields to search by

# EnhancementHistory Retrieve, Update, Destroy API
class EnhancementHistoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EnhancementHistory.objects.all()
    serializer_class = EnhancementHistorySerializer


# class ProjectFileListCreateView(generics.ListCreateAPIView):
#     """View to upload and list project files"""
#     queryset = ProjectFile.objects.all()
#     serializer_class = MultipleProjectFileUploadSerializer
#     filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
#     search_fields = ["project__project_name", "file"]
#     ordering_fields = "__all__"

# class ProjectFileRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     """View to retrieve, update, and delete project files"""
#     queryset = ProjectFile.objects.all()
#     serializer_class = MultipleProjectFileUploadSerializer
 

class ProjectFileListCreateView(generics.ListCreateAPIView):
    """View to upload and list project files"""
    queryset = ProjectFile.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["project__project_name", "file"]
    ordering_fields = "__all__"

    def get_serializer_class(self):
        if self.request.method == "POST":
            return MultipleProjectFileUploadSerializer
        return ProjectFileSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file_instances = serializer.save()
        return Response(ProjectFileSerializer(file_instances, many=True).data, status=status.HTTP_201_CREATED)


class ProjectFileRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """View to retrieve, update, and delete individual project files"""
    
    queryset = ProjectFile.objects.all()
    serializer_class = ProjectFileSerializer