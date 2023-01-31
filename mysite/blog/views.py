from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse

from .models import Article, Comment



def index(request):
    latest_articles_list = Article.objects.order_by('-article_date')[:10]
    context = {
        'latest_articles_list':latest_articles_list
    }
    return render(request, 'blog/index.html', context)

def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    comments_list = Comment.objects.filter(comment_article_id=article.id).order_by('-comment_date')
    context = {
        'article': article,
        'comments_list': comments_list,
    }
    try:
        if request.POST['author'] != '' and request.POST['text'] != '':
            new_comment = Comment(
                comment_author=request.POST['author'],
                comment_text=request.POST['text'],
                comment_date=timezone.now(),
                comment_article_id=article_id,
            )
            new_comment.save()
    except KeyError:
        return render(request, 'blog/detail.html', context)
    return render(request, 'blog/detail.html', context)
