from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm


# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    context = {'posts' : posts }
    return render (request, 'blog/post_list.html',context)

def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        postTempt = form.save()
        if 'image'in request.FILES:
            postTempt.image = request.FILES.get('image')
            postTempt.save()
        return redirect ('home')
    context = {
        'form':form
    }
    
    return render (request, 'blog/post_create.html',context)


def post_update(request, id):
    post = Post.objects.get(id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('home')
    context = {
        'form':form
    }
    
    return render (request, 'blog/post_update.html',context)

def post_delete(request, id):
    post = Post.objects.get(id=id)
    if request.POST :
        post.delete()
        return redirect('home')
    context = {
        'form':post
    }
    
    return render (request, 'blog/post_delete.html',context)
    


