from rest_framework import serializers
from .models import ProjectDetail, Developer, Task, TaskComment,BugHistory , EnhancementHistory




class ProjectDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectDetail
        fields = '__all__'
        
class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = '__all__'



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

