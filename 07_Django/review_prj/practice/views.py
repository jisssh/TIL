from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import Posting, Comment


# create
@require_http_methods(['GET', 'POST'])
def posting_create(request):
    if request.method == 'POST':
        posting = Posting()
        posting.title = request.POST.get('title')
        posting.content = request.POST.get('content')
        posting.save()
        return redirect('board_ad:posting_detail', posting.id)
    else:
        return render(request, 'practice/new.html')


# Read
@require_http_methods(['GET'])
def posting_list(request):
    postings = Posting.objects.all()
    return render(request, 'practice/list.html', {
        'postings': postings,
    })


@require_http_methods(['GET'])
def posting_detail(request, posting_id):
    # posting = Posting.objects.get(id=id)
    posting = get_object_or_404(Posting, id=posting_id)
    comments = posting.comment_set.all()
    return render(request, 'practice/detail.html', {
        'posting': posting,
        'comments': comments,
    })


# Update
def posting_update(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    if request.method == "POST":
        posting.title = request.POST.get('title')
        posting.content = request.POST.get('content')
        posting.save()
        return redirect('board_ad:posting_detail', posting_id=posting.id)
    else:
        return render(request, 'practice/edit.html', {'posting': posting})


@require_http_methods(['GET', 'POST'])
def posting_delete(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    posting.delete()
    return redirect('board_ad:posting_list')


# comment - Create
@require_http_methods(['POST'])
def comment_create(request, posting_id):
    posting = get_object_or_404(Posting, posting_id)
    comment = Comment()
    comment.posting = Posting.objects.get(posting_id)
    comment.content = request.POST.get('comment')
    comment.save()
    return redirect('board_ad:posting_detail', posting_id)


@require_http_methods(['POST'])
def comment_delete(request, posting_id, comment_id):
    posting = get_object_or_404(Posting, id=posting_id)
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return redirect('board_ad:posting_detail', posting_id=posting.id)
