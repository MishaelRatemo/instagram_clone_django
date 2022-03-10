from .models import Profile,Post
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['author',
                  'date_posted',
                  'liked',
                  ]
        
class UserDetailsForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        