from unicodedata import name
from django.urls import path
from . import views
urlpatterns = [
    path('', views.insta, name='index' ),
    path('logout', views.logout, name='logout'),
    path('post', views.post_data , name='post'),
    path('explore', views.explore , name='explore'),
    path('comment/<int:id>/', views.comments, name='comment'),
    # path('like/<int:id>/', views.likes, name='like'),
    path('like', views.like_post, name='likes'),
    path('profile',  views.profile , name='profile')
    
    
]