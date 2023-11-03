from django.db import models
from django.contrib.auth.models import User


class Articles(models.Model):
    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("published", "Published"),
    )

    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, unique=True)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")
    image = models.ImageField(default='default.jpg', blank=True)

    def __str__(self):
        return self.title
    
    def snippet(self):
        return self.content[:20] + " ..."
    
    def word_snippet(self):
        word_list = self.content.split()
        result = ' '.join(word_list[:10]) + " ..."
        return result
