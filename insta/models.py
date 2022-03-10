from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField( upload_to='profiles_photos/')
    bio = models.TextField(max_length=100)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save_profile(self):
        super().save()

    @classmethod
    def get_profile(cls):
        profile = Profile.objects.all()
        return profile

    @classmethod
    def find_profile(cls,search_term):
        profile = Profile.objects.filter(user__username__icontains=search_term)

        return profile


class Post(models.Model):
    image = models.ImageField(upload_to='photos/')
    title = models.CharField(max_length=160)
    description = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=True, related_name='author')
    liked = models.ManyToManyField(User, default=None, blank=True, related_name='liked')

    def __str__(self):
        return self.title

  
    @property
    def number_of_likes(self):
        return self.liked.all().count()
    
class Comment(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
# class Likes(models.Model):
#     like_id = models.ForeignKey(Post, on_delete = models.CASCADE)
#     like_user = models.ForeignKey(User, on_delete = models.CASCADE)
    
#     def __str__(self):
#         return self.like_user

class Like(models.Model):
    post= models.ForeignKey(Post, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.post