from django.urls import path
from . import views
urlpatterns = [
    path('', views.insta, name='index' ),
    path('logout', views.logout, name='logout'),
]