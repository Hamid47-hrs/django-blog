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

    def __str__(self):
        return self.title
