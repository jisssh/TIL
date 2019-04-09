from django.shortcuts import render, redirect
from .models import Posting, Comment


def posting_list(request):
    postings = Posting.objects.all()
    return render(request, 'practice/list.html', {
        'postings': postings,
    })

def posting_detail(request, id):
    posting = Posting.objects.get(id=id)
    return render(request, 'practice/detail.html', {
        'posting': posting,
    })