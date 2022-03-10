
from multiprocessing import context

from django.shortcuts import redirect, render, HttpResponseRedirect
from django.contrib.auth import logout as auth_logout
from django.contrib import  messages
from django.contrib.auth.decorators import login_required

from .forms import PostForm, UserDetailsForm
from insta.models import Post,Comment,Like
from django.contrib.auth.models import User



# Create your views here.
@login_required(login_url='/accounts/login/')
def insta(request):
   posts=Post.objects.all()
   user = request.user
   comments = ''
   
   try:
         comments = Comment.objects.all()
   except:
         comments = 'No comments'
   context = {
      'title':'Instagram',
      'posts' : posts, 
      'comments': comments,
      'user':user,
   }
   return render(request, 'index.html', context)

def logout(request):
    auth_logout(request)
    messages.success(request, 'Logged out successfully')
    return HttpResponseRedirect('/')
 
def post(request):
   user = request.user
   form = PostForm()
   if request.method == 'POST':
         form = PostForm(request.POST, request.FILES)
         if form.is_valid():
               post.save()
         return redirect('index')
   else:
         form = PostForm()
   return HttpResponseRedirect('index')

def post_data(request):
      user = request.user
      form = PostForm()      
      if request.method == 'POST':
                  form = PostForm(request.POST, request.FILES)
                  if form.is_valid():
                        form.save()  
      context = {
            'form' : form
      } 
      return render(request, 'post.html', context) 
         
def explore(request):
      explores=Post.objects.all()
      context = {'title':'Explore','explores' : explores }
      return render(request, 'explore.html', context)

def comments(request,id):
      if request.method == 'POST':
            comment =request.POST['commentname']
            post = Post.objects.get(id=id)
            user = request.user
            new_comment = Comment(content=comment,post=post,author=user)
            new_comment.save()
      
            return redirect('/')
      
# def likes(request,id):
#            if request.method == 'POST':
#                   post = Post.objects.get(id=id)
#                   user = request.user
#                   try:
#                        get_like = Likes.objects.get(like_id_id=post, like_user_id=user) 
#                        get_like.delete()
#                   except:
#                         new_like = Likes(like_id=id, like_user=user)
#                         new_like.save()
                  
#                   return redirect('/')
            
            
def like_post(request):
      user = request.user
      if request.method == 'POST':
            post_id = request.POST.get('post_id')
            post_obj = Post.objects.get(id=post_id)
            if user in post_obj.liked.all():
                  post_obj.liked.remove(user)
            else:
                 post_obj.liked.remove(user)
            like, created = Like.objects.get_or_create(user=user,post_id=post_id)
            like.save()
      return redirect('/')

def profile(request):
      posts=Post.objects.all()
      current_user = request.user
      
      if request.method == 'POST':
            form = UserDetailsForm(request.POST, request.FILES)
            
            if form.is_valid():
                  profile = form.save(commit=False)
                  profile.user = current_user
                  profile.save()        
            return redirect('profile')

      else:
            form = UserDetailsForm()
      context ={
            "form":form,
            "posts":posts,
      }            
    
      return render(request, 'profile.html',context)

      

   