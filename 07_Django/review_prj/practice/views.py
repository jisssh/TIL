from django.shortcuts import render, redirect
from .models import Article
# Create your views here.


def practice_new(request):
    return render(request, 'practice/new.html')


def practice_create(request):
    article = Article()
    article.title = request.POST.get('input_title')
    article.content = request.POST.get('input_content')
    article.save()
    return redirect(f'/practice/practice/{article.id}')


def practice_list(request):
    articles = Article.objects.all()
    return render(request, 'practice/list.html',{
        'articles': articles
    })


def practice_detail(request, id):
    article = Article.objects.get(id=id)
    return render(request, 'practice/detail.html', {
        'article': article
    })


def practice_edit(request, id):
    article = Article.objects.get(id=id)
    return render(request, 'practice/edit.html', {
        'article': article
    })


def practice_update(request, id):
    article = Article.objects.get(id=id)
    article.title = request.POST.get('input_title')
    article.content = request.POST.get('input_content')
    article.save()
    return redirect(f'/practice/practice/{article.id}')


def practice_delete(request, id):
    article = Article.objects.get(id=id)
    article.delete()
    return redirect('/practice/practice/')