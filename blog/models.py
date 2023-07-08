from django.db import models
from django.urls import reverse
# Create your models here.

class Article(models.Model):
    
        title = models.CharField(max_length=100)
        content = models.TextField()
        active = models.BooleanField(default=True)
    
        class Meta:
            verbose_name = ("article")
            verbose_name_plural = ("articles")
    
        def __str__(self):
            return self.title
    
        def get_absolute_url(self):
            return reverse("article_detail", kwargs={"pk": self.pk})
    