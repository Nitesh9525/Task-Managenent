from rest_framework import serializers
from .models import ProjectDetail, Developer, Task, TaskComment,BugHistory , EnhancementHistory





        
class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = '__all__'

# class ProjectDetailSerializer(serializers.ModelSerializer):
#     developers = DeveloperSerializer(many=True, read_only=True)  # Nested developer serializer

#     class Meta:
#         model = ProjectDetail
#         fields = '__all__'

class ProjectDetailSerializer(serializers.ModelSerializer):
    developers = DeveloperSerializer(many=True, read_only=True)  # Nested Developer data in response
    developer_ids = serializers.ListField(
        child=serializers.IntegerField(), write_only=True, required=False
    )  # Accept a list of developer IDs when creating/updating

    class Meta:
        model = ProjectDetail
        fields = '__all__'

    def create(self, validated_data):
        developer_ids = validated_data.pop('developer_ids', [])  # Get developer IDs if provided
        project = ProjectDetail.objects.create(**validated_data)
        project.developers.set(developer_ids)  # Assign developers to the project
        return project

    def update(self, instance, validated_data):
        developer_ids = validated_data.pop('developer_ids', None)
        instance = super().update(instance, validated_data)
        if developer_ids is not None:
            instance.developers.set(developer_ids)  # Update project-developers relation
        return instance
    
# class DeveloperWithProjectsSerializer(serializers.ModelSerializer):
#     projects = ProjectDetailSerializer(many=True, read_only=True)  # Include associated projects

#     class Meta:
#         model = Developer
#         # fields = '__all__'
#         fields = ['developer_id', 'projects', 'full_name', 'email', 'mobile_number', 'password_hash', 'created_at', 'company', 'monthly_rate', 'address']

#     def get_projects(self, obj):
#         return obj.projects.values_list('project_id', flat=True)



# class ProjectDetailSerializer(serializers.ModelSerializer):
#     developers = DeveloperSerializer(many=True, read_only=False)  # Allow modifying developers
    
#     class Meta:
#         model = ProjectDetail
#         fields = '__all__'

#     def update(self, instance, validated_data):
#         developers_data = validated_data.pop('developers', None)
        
#         # Update the project fields as usual
#         instance = super().update(instance, validated_data)
        
#         if developers_data is not None:
#             # Update many-to-many relationship (developers)
#             instance.developers.set([developer['developer_id'] for developer in developers_data])
        
#         return instance



class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class TaskCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskComment
        fields = '__all__'

class BugHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BugHistory
        fields = '__all__'

class EnhancementHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EnhancementHistory
        fields = '__all__'

from .models import ProjectFile

class ProjectFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectFile
        fields = '__all__'


class MultipleProjectFileUploadSerializer(serializers.Serializer):
    project = serializers.PrimaryKeyRelatedField(queryset=ProjectDetail.objects.all())
    files = serializers.ListField(
        child=serializers.FileField(),
        write_only=True
    )

    def create(self, validated_data):
        project = validated_data["project"]
        files = validated_data["files"]
        file_instances = [ProjectFile.objects.create(project=project, file=file) for file in files]
        return file_instances


