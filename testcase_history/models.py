from django.db import models
from test_suite.models import ProjectTestSuite

# Create your models here.
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
        