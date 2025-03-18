from rest_framework import serializers
from .models import ProjectDetail, Developer, Task, TaskComment #, EnhancementHistory

class ProjectDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectDetail
        fields = '__all__'


class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class TaskCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskComment
        fields = '__all__'

# class BugHistorySerializer(ModelSerializer):
#     class Meta:
#         model = BugHistory
#         fields = '__all__'

# class EnhancementHistorySerializer(ModelSerializer):
#     class Meta:
#         model = EnhancementHistory
#         fields = '__all__'
