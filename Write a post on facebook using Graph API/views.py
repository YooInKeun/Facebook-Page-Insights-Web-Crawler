from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
import facebook #facebook-sdk 설치 및 패키지에 추가 후 import facebook

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()

            #request.POST 값 안에서 text란에 쓰여진 string만 따로 추출하기 : message

            temp = request.POST
            str_request = str(temp)
            print(str_request)
            str_text = 'text'
            str_bracket = '>'

            f = str_request.find(str_text)
            f2 = str_request.find(str_bracket)

            message = str_request[f+9:f2-3] #message는 text란에 쓰여진 string

            print(message) #테스트

            #facebook에서 access token을 발급받아, put_object로 facebook 페이지 게시판에 message 내용을 포스팅

            token = 'EAAEHEQKJmAMBAJqTYWeeBuNvRcZBh8YLQjlq14VR9hj5Yww5RjnSx5H5sxOmjBvZBgHmGhwdZAKxTmH5gmqbUJkUCTxOF5yHlcMZBmgvEZCAZAPe4lFWAGJgwgYOsdYgUUEKW3P15IDtVZA9csSgrZAhid3gZC3UHjYZAC3BZBGtXqNtPU3K1bL3XP5ja2vZAC0KfZANejyzw8RmbXRvYJhYPpExt'
            fb = facebook.GraphAPI(access_token=token)
            fb.put_object(parent_object='me', connection_name='feed', message=message)

            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

# Create your views here.
