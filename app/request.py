from os import name
from app import app
import urllib.request,json

from app.article_test import Article
from .models import source

Source = source.Source


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

def process_results(sources_list):
    '''
    Function  that processes the sources and transform them to a list of Objects

    Args:
        sources_list: A list of dictionaries that contain movie details

    Returns :
        sources_results: A list of movie objects
    '''

    sources_results = []
    for source_item in sources_list:
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

        article_object = None
        if article_response:
            source = article_response.get('source')
            author = article_response.get('author')
            title = article_response.get('title')
            description = article_response.get('description')
            url = article_response.get('url')
            urlToImage = article_response.get('urlToImage')
            publishedAt = article_response.get('publishedAt')
            content = article_response.get('content')

            article_object = Article(source, author, title, description, url, urlToImage, publishedAt, content)
            
    return article_object
