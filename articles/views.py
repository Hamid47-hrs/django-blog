from django.shortcuts import HttpResponse, render, redirect
from django.contrib.auth.decorators import login_required
from . import models
from . import forms


def articles_list(request):
    articles = models.Articles.objects.filter(status="published").order_by(
        "-created_date"
    )
    context = {
        "articles": articles,
    }

    return render(request, "articles_list.html", context=context)


def articles_detail(request, slug):
    article = models.Articles.objects.get(slug=slug)

    context = {
        "article": article,
    }

    return render(
        request,
        "article_detail.html",
        context=context,
    )


@login_required(login_url="/accounts/login")
def create_article(request):
    if request.method == "POST":
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid:
            form_instance = form.save(commit=False)
            form_instance.author = request.user
            form_instance.save()

            return redirect("articles:list")

    else:
        form = forms.CreateArticle()

    return render(request, "create_article.html", {"form": form})
