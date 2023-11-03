from django.shortcuts import render, HttpResponse
from . import models


def articles_list(request):
    articles = models.Articles.objects.filter(status="published").order_by(
        "-created_date"
    )
    context = {
        "articles": articles,
    }

    return render(request, "articles/articles_list.html", context=context)


def articles_detail(request, slug):
    article = models.Articles.objects.get(slug=slug)

    context = {
        "article": article,
    }

    return render(
        request,
        "articles/article_detail.html",
        context=context,
    )
