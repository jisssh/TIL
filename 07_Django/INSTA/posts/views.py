from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from .models import Post, Image
from .forms import PostModelForm, ImageModelForm, CommentModelForm


@login_required()
@require_http_methods(['GET', 'POST'])
def create_post(request):
    # POST 방식으로 넘온 Data 를 ModelForm 에 넣는다.
    if request.method == 'POST':
        # POST 방식으로 넘온 Data 를 ModelForm 에 넣는다.
        # ModelForm(data, files)
        post_form = PostModelForm(request.POST)
        # 위 코드가 아래 코드를 한방에 넣어줌
        # post = Post()
        # post.content = request.POST.get('content')
        # post.title = 등등등
        # post.image = request.FILES.get('image')
        if post_form.is_valid():  # Data 검증을 한다.
            # 통과하면 저장한다.
            post = post_form.save(commit=False)
            post.uploader = request.user
            post.save()
            for image in request.FILES.getlist('file'):
                request.FILES['file'] = image
                image_form = ImageModelForm(files=request.FILES)
                if image_form.is_valid():
                    image = image_form.save(commit=False)
                    image.post = post
                    image.save()
            # 저장하고, redirect
            return redirect('posts:post_list')
        else:
            # 실패하면, 다시 data 입력 form 을 준다.
            pass
    # GET 방식으로 요청이 오면,
    else:
        # 새로운 Post 용 form 을 만든다.
        post_form = PostModelForm()
    image_form = ImageModelForm()
    # 사용자에게 html 과 form 을 같이 넘긴다.
    return render(request, 'posts/form.html', {
        'post_form': post_form,
        'image_form': image_form,
    })


@login_required()
@require_http_methods(['GET', 'POST'])
def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    # 지금 수정하려는 post 작성자가 요청보낸 사람이냐?
    if post.uploader == request.user:
        if request.method == 'POST':
            post_form = PostModelForm(request.POST, instance=post)
            if post_form.is_valid():
                post_form.save()
                return redirect('posts:post_list')
        else:
            post_form = PostModelForm(instance=post)
        return render(request, 'posts/form.html', {
            'post_form': post_form,
        })
    # 작성자와 요청 보낸 user 가 다르다면,
    else:
        # 403 : Forbidden 금지됨!
        return redirect('posts:post_list')


@login_required()
@require_http_methods(['GET', 'POST'])
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.uploader == request.user:
        post.delete()
    return redirect('posts:post_list')


@require_GET
def post_list(request):
    posts = Post.objects.all()
    comment_form = CommentModelForm()
    return render(request, 'posts/list.html', {
        'posts': posts,
        'comment_form': comment_form,
    })


@login_required
@require_POST
def creat_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    form = CommentModelForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.commenter = request.user
        comment.post = post
        comment.save()
        return redirect('posts:post_list')
    # Todo: else => comment 가 유효하지 않다면 어떻게 하지?

# @login_required
# @require_POST
# def create_comment(request, post_id):
#     post = get_object_or_404(Post, id=post_id)
#     comment_form = CommentModelFrom(data=request.POST)
#     if comment_form.is_valid():
#         comment = comment_form.save(commit=False)
#         comment.user = request.user
#         comment.post = post
#         comment.save()
#         return redirect('posts:post_list')
#     # TODO: else: => if comment is not valid, then what?```