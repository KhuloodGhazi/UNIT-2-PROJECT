from django.db import models

# Create your models here.

class Project(models.Model):
    class CategoryChoices(models.TextChoices):
        MOBILE_APP = 'Mobile App', 'Mobile App'
        WEBSITE = 'Website', 'Website'

    project_name = models.CharField(max_length=1024) 
    project_brief = models.TextField(blank=True, null=True, default='') 
    project_model = models.URLField(max_length=1024, blank=True, null=True, default='')
    project_explanation = models.TextField(blank=True, null=True, default='')
    read_more_link = models.URLField(max_length=1024, blank=True, null=True, default='')
    year = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='images/' , default="")
    create_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(
        max_length=20,
        choices=CategoryChoices.choices,
    )

    def __str__(self):
        return self.project_name

