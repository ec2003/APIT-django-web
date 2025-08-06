from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project_name
    
    class Meta:
        indexes = [
            models.Index(fields=['user']),
            models.Index(fields=['project_name']),
        ]
        ordering = ['-created_at']

class ProjectTestSuite(models.Model):
    project = models.ForeignKey(UserProject, on_delete=models.CASCADE)
    test_suite_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.test_suite_name
    
    class Meta:
        indexes = [
            models.Index(fields=['project']),
            models.Index(fields=['test_suite_name']),
        ]
        ordering = ['-created_at']

class TestCaseHistory(models.Model):
    test_suite = models.ForeignKey(ProjectTestSuite, on_delete=models.CASCADE)    
    test_case = models.JSONField()  # Assuming test_case is a JSON object
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.test_case}"
    
    class Meta:
        indexes = [
            models.Index(fields=['test_suite']),
        ]
        ordering = ['-created_at']