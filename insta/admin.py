from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 
from django.urls import reverse

class Post(models.Model):
    image = models.ImageField(upload_to='uploads/')
    title = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    posted_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes=models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('instagram-home')
    
    @property
    def number_of_comments(self):
        return Comment.objects.filter(post=self).count()
    
class Comment(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)