
from app import app
import urllib.request,json

from app.article_test import Article
from .models import source, article

Source = source.Source
Article = article.Article


api_key = app.config['NEWS_API_KEY']

base_url = app.config['NEWS_API_URL']
article_url = app.config['ARTICLES_API_URL']


def get_news_sources():
    '''
    Function that gets the json response to our url request
    '''
    get_news_sources_url = base_url.format(api_key)

    with urllib.request.urlopen(get_news_sources_url) as url:
        get_source_details = url.read()
        get_news_response = json.loads(get_source_details)

        sources_results = None

        if get_news_response['sources']:
            sources_results_list = get_news_response['sources']
            sources_results = process_results(sources_results_list)

    return sources_results

def process_results(source_list):
    '''
    Function  that processes the sources and transform them to a list of Objects

    Args:
        sources_list: A list of dictionaries that contain movie details

    Returns :
        sources_results: A list of movie objects
    '''

    sources_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        category = source_item.get('category')
        url = source_item.get('url')
        language = source_item.get('language')
        country = source_item.get('country')

        sources_object = Source(id, name,  description, url, category, language, country)
        sources_results.append(sources_object)

    return sources_results

def get_article(id):

    get_article_url = article_url.format(id, api_key)

    with urllib.request.urlopen(get_article_url) as url:
        article_data = url.read()
        article_response = json.loads(article_data)

        article_results = None

        if article_response['articles']:
            article_results_list = article_response['articles']
            article_results = process_result(article_results_list)


    return article_results

def process_result(article_list):
    '''
    Function  that processes the articles and transform them to a list of Objects

    Args:
        article_list: A list of dictionaries that contain movie details

    Returns :
        article_results: A list of movie objects
    '''

    article_results = []
    for article_item in article_list:
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')
        content = article_item.get('content')

        article_object = Article(author, title, description, url, urlToImage, publishedAt, content)
        article_results.append(article_object)

    return article_results
