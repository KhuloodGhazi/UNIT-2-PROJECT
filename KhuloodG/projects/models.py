from django.db import models

# Create your models here.

class Project(models.Model):
    class CategoryChoices(models.TextChoices):
        MOBILE_APP = 'Mobile App', 'Mobile App'
        WEBSITE = 'Website', 'Website'

    project_name = models.CharField(max_length=1024) 
    project_brief = models.TextField() 
    project_model = models.URLField(max_length=1024)
    create_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(
        max_length=20,
        choices=CategoryChoices.choices,
    )
