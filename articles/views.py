from django.shortcuts import render
from . import models


def articles_list(request):
    articles = models.Articles.objects.filter(status="published").order_by(
        "created_date"
    )
    context = {
        "articles": articles,
    }

    return render(request, "articles/articles_list.html", context=context)
