from django.db import models
from project.models import UserProject

# Create your models here.
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
        unique_together = ['project', 'test_suite_name']