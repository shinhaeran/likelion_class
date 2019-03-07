from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone
# Create your views here.


def blog(request):
    blogs = Blog.objects
    return render(request, 'blog/blog.html', {'blogs': blogs})
    # return render(request, 'blog/home.html')

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request,'blog/detail.html',{'blog':blog_detail})

def new(request):
    return render(request, 'blog/new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))

# def edit(request, blog_id):
#     blog = get_object_or_404(Blog, pk = blog_id)
#     if request.method == 'POST':
#         pass
#     else:
#         blog.title = request.GET['title']
#         blog.body = request.GET['body']
#         blog.pub_date = timezone.datetime.now()
#         blog.save()

#     return render(request, 'blog/edit.html')

def delete(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    blog.delete()
    return redirect('/blog/')
    
