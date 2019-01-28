from django.db import models
from django.utils import timezone
from django.http import HttpResponse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(blank=True, null=True)
    content = models.TextField()


    def publish(self):
        self.date_updated = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    date_created = models.DateTimeField('date published')
    content =models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return 'Comment: {}'.format(self.post)
