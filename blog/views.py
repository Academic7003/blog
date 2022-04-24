from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from blog.models import BlogPost
from blog.forms import *
from django.http import HttpResponse




def blog_view(request):
    blog = BlogPost.objects.all()
    
    context = {
        'blog_list':blog,

    }
    return render(request, 'blog.html' , context )

def create_blog_view(request): 

    context = {}
    form = BlogModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        form = BlogModelForm()

    context['form'] = form
    return render(request, 'create-blog.html', context)



def detail_blog_view(request, slug):
    context = {}

    blog_post = get_object_or_404(BlogPost, slug=slug)
    context['blog_post'] = blog_post

    return render(request, 'detail.html', context)




def edit_blog_view(request, slug):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('login')

    blog_post = get_object_or_404(BlogPost, slug=slug)

    if blog_post.author != user:
        return HttpResponse('Aftorlik huquqi yo`q')

    if request.POST:
        form = BlogUpdateForm(request.POST or None, request.FILES or None, instance=blog_post)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            context['success_message'] = "Updated"
            blog_post = obj
            return redirect("blog:blogs")
    form = BlogUpdateForm(
        initial={
            'title':blog_post.title,
            'body': blog_post.body,
            'image': blog_post.image,

        }
    )

    context['form'] = form
    return render(request, 'edit.html', context)


def delete_blog_view(request, slug):
    # dictionary for initial data with
    # field names as keys
    context ={}

    user = request.user
    if not user.is_authenticated:
        return redirect('login')

    obj = get_object_or_404(BlogPost, slug = slug)

    if obj.author != user:
        return HttpResponse('Aftorlik huquqi yo`q')

    
 
    # fetch the object related to passed id
    
 
 
    if request.POST:
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page

        return redirect("blog:blogs")
    context['form']=obj.title
 
    return render(request, "delete.html", context)


# def comment_blog_view(request,):
#     context = {}

#     blog_post = get_object_or_404(BlogPost)
#     context['comments'] = blog_post

#     return render(request, 'detail.html', context)