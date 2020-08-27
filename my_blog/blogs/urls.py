from django.urls import path, re_path, include
from django.views.generic import ListView, DetailView
from . import views
from blogs.models import Blog

urlpatterns = [
    #path('', views.homepage),
    path('addblog/', views.add_blog),
    path('', ListView.as_view(queryset=Blog.objects.all().order_by('-publish_date'), template_name = 'blogs/posts.html')),
    re_path(r'^blogs/(?P<pk>\d+)$', DetailView.as_view(model=Blog, template_name='blogs/post.html'))
]