from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    sample_url = models.TextField()
    project_url = models.TextField()
    project_img = models.TextField()
    pages_img = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title
