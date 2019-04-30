from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post, Image, Comment, HashTag
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

            # create HashTag => <input name-'tags' /> #hi #ssafy #20층
            content = post_form.cleaned_data.get('content')
            words = content.split(' ')  # 띄어쓰기 기준으로 split 한다.
            for word in words:
                if word[0] == '#':
                    word = word[1:]
                    tag = HashTag.objects.get_or_create(content=word)   # (HashTagObj, True / False)
                    post.tags.add(tag[0])
                    if tag[1]:  # 태그가 처음 만들어진거라면, 메세지 추가!
                        messages.add_message(request, messages.SUCCESS, f'{tag[0].content} 태그를 처음으로 추가하셨어요!ღ')

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
                # update HashTag
                post.tags.clear()   # 기존의 태그 다 날리기
                content = post_form.cleaned_data.get('content')
                words = content.split(' ')  # 띄어쓰기 기준으로 split 한다.
                for word in words:
                    if word[0] == '#':
                        word = word[1:]
                        tag = HashTag.objects.get_or_create(content=word)  # (HashTagObj, True / False)
                        post.tags.add(tag[0])
                        if tag[1]:  # 태그가 처음 만들어진거라면, 메세지 추가!
                            messages.add_message(request, messages.SUCCESS, f'{tag[0].content} 태그를 처음으로 추가하셨어요!ღ')

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
        # return redirect('posts:post_list')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/insta/'))
    # Todo: else => comment 가 유효하지 않다면 어떻게 하지?


@login_required
@require_http_methods(['GET', 'POST'])
def delete_comment(request, post_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if comment.commenter == request.user:
        comment.delete()
    return redirect('posts:post_list')


@login_required()
@require_POST
def toggle_like(request, post_id):
    user = request.user
    post = get_object_or_404(Post, id=post_id)
    # if post.likes.filter(id=user.id).exist():   # 찾으면, [value] / 없으면, []
    #     post.likes.remove(user)
    # 위 아래 같은 코드임 !
    if user in post.likes.all():
        post.likes.remove(user)
    else:
        post.likes.add(user)
    return redirect('posts:post_list')


@require_GET
def tag_posts_list(request, tag_name):
    tag = get_object_or_404(HashTag, content=tag_name)
    posts = tag.posts.all()
    comment_form = CommentModelForm()
    return render(request, 'posts/list.html', {
        'posts': posts,
        'comment_form': comment_form,
        'h1': f'#{tag} 를 포함한 posts 입니다.'
    })
