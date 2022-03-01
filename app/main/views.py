
from flask import render_template, request,redirect,url_for
from . import main
from ..request import get_news_sources, get_article, search_article

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    news_sources = get_news_sources()
    title = 'News Sources'
    search_source = request.args.get('source_query')

    if search_source:
        return redirect(url_for('.search', name=search_source))
    else:
        return render_template('index.html', title = title, sources = news_sources)

@main.route('/article/<id>')
def article(id):
    '''
    View article page function that returns the news articles page and its details
    '''
    news = get_article(id)
    title = 'News Articles'
    return render_template('article.html', title = title, name = id, news = news)

@main.route('/search/<name>')
def search(name):
    '''
    View function to display the search results
    '''
    source_name_list = name.split(" ")
    source_name_format = "+".join(source_name_list)
    searched_source = search_article(source_name_format)
    title = f'search results for {name}'
    return render_template('search.html',sources = searched_source)