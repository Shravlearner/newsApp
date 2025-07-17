from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.dateparse import parse_datetime
from django.conf import settings
from .models import Search, Article
import requests

@login_required
def search_view(request):
    latest_articles = []

    if request.method == 'POST':
        query = request.POST.get('query')
        search = Search.objects.create(user=request.user, query=query)

        # Call NewsAPI for search results
        url = (
            f'https://newsapi.org/v2/everything?'
            f'q={query}&'
            f'sortBy=publishedAt&'
            f'apiKey=ce94c74c86014a1f92d0a902660a74cf'
        )
        response = requests.get(url)
        data = response.json()

        articles = data.get('articles', [])
        for item in articles:
            Article.objects.create(
                search=search,
                title=item.get('title'),
                description=item.get('description'),
                url=item.get('url'),
                url_to_image=item.get('urlToImage'),
                published_at=parse_datetime(item.get('publishedAt')),
                source_name=item.get('source', {}).get('name', '')
            )
        print(articles)
        return redirect('search:results', search_id=search.id)

    else:
    # Fetch top headlines for latest news display
        url = (
            f'https://newsapi.org/v2/top-headlines?'
            f'language=en&'
            f'apiKey=ce94c74c86014a1f92d0a902660a74cf'
        )
        response = requests.get(url)
        data = response.json()
        print("Latest Global News Response:", data)
        latest_articles = data.get('articles', [])


    return render(request, 'search/search.html', {
        'latest_articles': latest_articles
    })


@login_required
def refresh_view(request, search_id):
    search = get_object_or_404(Search, id=search_id, user=request.user)

    # Delete old articles
    search.articles.all().delete()

    # Fetch new articles
    url = (
        f'https://newsapi.org/v2/everything?'
        f'q={search.query}&'
        f'sortBy=publishedAt&'
        f'apiKey=ce94c74c86014a1f92d0a902660a74cf'
    )
    response = requests.get(url)
    data = response.json()
    print("Refreshing articles for query:", search.query)

    for item in data.get('articles', []):
        Article.objects.create(
            search=search,
            title=item.get('title'),
            description=item.get('description'),
            url=item.get('url'),
            url_to_image=item.get('urlToImage'),
            published_at=parse_datetime(item.get('publishedAt')),
            source_name=item.get('source', {}).get('name', '')
        )

    return redirect('search:results', search_id=search.id)


@login_required
def history_view(request):
    searches = Search.objects.filter(user=request.user).order_by('-searched_at')
    return render(request, 'search/history.html', {'searches': searches})


@login_required
def results_view(request, search_id):
    search = get_object_or_404(Search, id=search_id, user=request.user)
    sort_order = request.GET.get('sort', 'desc')  # default is 'desc'

    if sort_order == 'asc':
        articles = search.articles.all().order_by('published_at')
    else:
        articles = search.articles.all().order_by('-published_at')

    context = {
        'search': search,
        'articles': articles,
        'current_sort': sort_order,
    }
    return render(request, 'search/results.html', context)
