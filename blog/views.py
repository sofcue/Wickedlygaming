from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Videos
from .forms import PostForm, VideoForm
from django.utils import timezone


# Create your views here.
def index(request):
    queryset = Post.objects.filter(status=1).order_by('-createdOn')
    template_name = 'index.html'
    return render(request, template_name, {'queryset': queryset})


def post_detail(request, slug):
    model = get_object_or_404(Post, slug=slug)
    template_name = 'post_detail.html'
    return render(request, template_name, {'post': model})


def about(request):
    return render(request, 'aboutme.html', {})


def post_list(request):
    queryset = Post.objects.filter(status=1).order_by('-createdOn')
    template_name = 'post_list.html'
    return render(request, template_name, {'queryset': queryset})


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.updatedOn = timezone.now()
            post.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm()
    template_name = 'post_edit.html'
    return render(request, template_name, {'form': form})


def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.updatedOn = timezone.now()
            post.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})


def videos(request):
    allItems = Videos.objects.all()

    return render(request, 'videos.html', {'videos': allItems})


def add_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('videos')
    else:
        form = VideoForm()
    template_name = 'video_edit.html'
    return render(request, template_name, {'video_form': form})
