from django.db import models

# Create your models here.
class BlogContent(models.Model):
    Title = models.CharField(max_length=200)
    Author = models.CharField(max_length=200)
    Slug = models.CharField(max_length=200, primary_key=True)
    Content = models.TextField()


#Post Endpoint (outside scope) consideration, how to ensure removal of slug from tag if blog post is edited in the future.
class Tags(models.Model):
    Slug = models.ForeignKey(BlogContent, on_delete=models.CASCADE)
    Tag = models.CharField(max_length=50, primary_key=True)