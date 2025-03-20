from django.urls import path
from . import views

urlpatterns = [
    # Project Detail URLs
    path('projects/', views.ProjectDetailListCreateView.as_view(), name='project-list-create'),
    path('projects/<int:pk>/', views.ProjectDetailRetrieveUpdateDestroyView.as_view(), name='project-retrieve-update-destroy'),

    # Developer URLs
    path('developers/', views.DeveloperListCreateView.as_view(), name='developer-list-create'),
    path('developers/<int:pk>/', views.DeveloperRetrieveUpdateDestroyView.as_view(), name='developer-retrieve-update-destroy'),

    # Task URLs
    path('tasks/', views.TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', views.TaskRetrieveUpdateDestroyView.as_view(), name='task-retrieve-update-destroy'),

    # Task Comment URLs
    path('task-comments/', views.TaskCommentListCreateView.as_view(), name='task-comment-list-create'),
    path('task-comments/<int:pk>/', views.TaskCommentRetrieveUpdateDestroyView.as_view(), name='task-comment-retrieve-update-destroy'),

    path('bug-history/', views.BugHistoryListCreateAPIView.as_view(), name='bug-history-list-create'),
    path('bug-history/<int:pk>/', views.BugHistoryRetrieveUpdateDestroyAPIView.as_view(), name='bug-history-retrieve-update-destroy'),
    path('enhancement-history/', views.EnhancementHistoryListCreateAPIView.as_view(), name='enhancement-history-list-create'),
    path('enhancement-history/<int:pk>/', views.EnhancementHistoryRetrieveUpdateDestroyAPIView.as_view(), name='enhancement-history-retrieve-update-destroy'),

    path('project-files/', views.ProjectFileListCreateView.as_view(), name='project-file-list-create'),
    path('project-files/<int:pk>/', views.ProjectFileRetrieveUpdateDestroyView.as_view(), name='project-file-detail'),
]
