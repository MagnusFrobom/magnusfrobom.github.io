# First, we need to create a new Django project and app
# Open a terminal and navigate to the directory where you want to create your project
$ django-admin startproject myproject
$ cd myproject
$ python manage.py startapp myapp

# Next, we need to create a model to represent the blog posts that we want to display
# Open myapp/models.py and add the following code:
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

# Now we need to create a view to display the list of blog posts
# Open myapp/views.py and add the following code:
from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all().order_by('-published_date')
    return render(request, 'myapp/post_list.html', {'posts': posts})

# Next, we need to create a template to render the list of blog posts
# Create a new file called post_list.html in the myapp/templates/myapp directory and add the following code:
<h1>List of Posts</h1>

{% for post in posts %}
    <h2>{{ post.title }}</h2>
    <p>{{ post.content }}</p>
    <p>Published on {{ post.published_date }}</p>
{% endfor %}

# Finally, we need to create a URL pattern to map to the view that we just created
# Open myapp/urls.py and add the following code:
from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.post_list, name='post_list'),
]

# Now we can run the development server and visit http://127.0.0.1:8000/posts/ to see the list of blog posts
$ python manage.py runserver
