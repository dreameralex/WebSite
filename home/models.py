from django.db import models

class Carousel(models.Model):
    image = models.ImageField(upload_to='carousel_images/')
    title = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=255, blank=True)
    link = models.URLField(blank=True)
    active = models.BooleanField(default=True)  # 添加active字段

    def __str__(self):
        return self.title if self.title else "Carousel Image"

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

