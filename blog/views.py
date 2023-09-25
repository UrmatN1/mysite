from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import Http404

# Create your views here.


def post_detail(request, id):
    try:
        post = get_object_or_404(Post,
                                 id=id,
                                 status=Post.Status.PUBLISHED)
    except Post.DoesNotExist:
        raise Http404("No Post Found")

    return render(request,"blog/detail.html",{'post': post})

def post_list(request):
    posts = Post.published.all()
    return render(request,"blog/list.html",{'posts': posts})
