from django.shortcuts import render, get_object_or_404
from .models import News, Category

def home(request):
    news_list = News.objects.order_by('-publication_date')[:10]  # publish_date yerine publication_date
    return render(request, 'news/index.html', {'news_list': news_list})


def news_list(request):
    news_list = News.objects.all()
    return render(request, 'news/news_list.html', {'news_list': news_list})


def category(request, id):
    category = get_object_or_404(Category, id=id)
    category_news = News.objects.filter(category=category).order_by('-publication_date')[:20]  # publish_date yerine publication_date
    return render(request, 'news/category.html', {'category': category, 'news': category_news})


def news_detail(request, id):
    news = get_object_or_404(News, id=id)
    related_news = News.objects.filter(category=news.category).exclude(id=news.id)[:3]
    return render(request, 'news/news_detail.html', {'news': news, 'related_news': related_news})

