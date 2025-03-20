from django.db import models



# class ProjectDetail(models.Model):
#     project_id = models.AutoField(primary_key=True)
#     project_name = models.CharField(max_length=100)
#     planned_start_date = models.DateTimeField()
#     planned_end_date = models.DateTimeField()
#     developers = models.ManyToManyField("Developer", related_name="projects")  # Many-to-Many Relationship

#     def __str__(self):
#         return self.project_name
  

# class Developer(models.Model):
#     developer_id = models.AutoField(primary_key=True)
#     project = models.ForeignKey(ProjectDetail, on_delete=models.CASCADE, null=True, blank=True) # remove null = True 
#     full_name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     mobile_number = models.CharField(max_length=20, blank=True)
#     password_hash = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     company = models.CharField(max_length=100, blank=True)
#     monthly_rate = models.FloatField(null=True, blank=True)
#     address = models.CharField(max_length=255, blank=True)

#     def __str__(self):
#         return self.full_name


class ProjectDetail(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=100)
    planned_start_date = models.DateTimeField(blank=True,null=True)
    planned_end_date = models.DateTimeField(blank=True,null=True)
    developers = models.ManyToManyField("Developer", related_name="projects",blank=True,null=True)  # Many-to-Many Relationship

    def __str__(self):
        return self.project_name
  

class Developer(models.Model):
    developer_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=20, blank=True)
    password_hash = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    company = models.CharField(max_length=100, blank=True)
    monthly_rate = models.FloatField(null=True, blank=True)
    address = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.full_name
    


class Task(models.Model):
    STATUS_CHOICES = [
        ('To Do', 'To Do'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('On-Hold', 'On-Hold'),
        ('Blocked', 'Blocked'),
    ]
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    task_id = models.AutoField(primary_key=True)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    project = models.ForeignKey(ProjectDetail, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='To Do')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    due_date = models.DateField(null=True, blank=True)
    planned_start_date = models.DateTimeField(null=True, blank=True)
    planned_end_date = models.DateTimeField(null=True, blank=True)
    actual_start_date = models.DateTimeField(null=True, blank=True)
    actual_end_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def delayed_start_by_days(self):
        if self.planned_start_date and self.actual_start_date:
            return (self.actual_start_date - self.planned_start_date).days
        return None

    @property
    def delayed_end_by_days(self):
        if self.planned_end_date and self.actual_end_date:
            return (self.actual_end_date - self.planned_end_date).days
        return None

    @property
    def total_number_of_day_taken(self):
        if self.actual_start_date and self.actual_end_date:
            return (self.actual_end_date - self.actual_start_date).days
        return None

    def _str_(self):
        return self.title  # String representation of the model

    def __str__(self):
        return self.title


class TaskComment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    project = models.ForeignKey(ProjectDetail, on_delete=models.CASCADE)
    comment_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.developer.full_name} on {self.task.title}"
    

class BugHistory(models.Model):
    bug_history_id = models.AutoField(primary_key=True)
    task = models.ForeignKey('Task', on_delete=models.CASCADE)
    updated_by = models.ForeignKey('Developer', on_delete=models.CASCADE)
    project = models.ForeignKey('ProjectDetail', on_delete=models.SET_NULL, null=True, blank=True)
    bug_description = models.TextField()
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'bug_history'

    def __str__(self):
        return f"Bug {self.bug_history_id} - Task {self.task.task_id}"

class EnhancementHistory(models.Model):
    enhancement_history_id = models.AutoField(primary_key=True)
    task = models.ForeignKey('Task', on_delete=models.CASCADE)
    updated_by = models.ForeignKey('Developer', on_delete=models.CASCADE)
    project = models.ForeignKey('ProjectDetail', on_delete=models.SET_NULL, null=True, blank=True)
    enhancement_description = models.TextField(null=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'enhancement_history'

    def __str__(self):
        return f"Enhancement {self.enhancement_history_id} - Task {self.task.task_id}"
    
# class ProjectFile(models.Model):
#     """Model to store multiple files for a project"""
#     file_id = models.AutoField(primary_key=True)
#     project = models.ForeignKey(ProjectDetail, on_delete=models.CASCADE, related_name="files")
#     file = models.FileField(upload_to='project_files/')
#     uploaded_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"File for {self.project.project_name} - {self.file.name}"
    



import os
from django.utils.text import slugify

def project_file_path(instance, filename):
    """Generate file path for uploaded files within a project-specific folder"""
    project_name = slugify(instance.project.project_name)
    return os.path.join(f'project_files/{project_name}', filename)

class ProjectFile(models.Model):
    """Model to store multiple files for a project"""
    file_id = models.AutoField(primary_key=True)
    project = models.ForeignKey(ProjectDetail, on_delete=models.CASCADE, related_name="files")
    file = models.FileField(upload_to=project_file_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"File for {self.project.project_name} - {self.file.name}"
