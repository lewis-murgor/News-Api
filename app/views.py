
from flask import render_template
from app import app
from .request import get_news_sources, get_article

@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    news = get_news_sources()
    title = 'News Sources'
    return render_template('index.html', title = title, news = news)

@app.route('/article/<id>')
def article(id):
    '''
    View article page function that returns the news articles page and its details
    '''
    article = get_article(id)
    title = 'News Articles'
    return render_template('article.html', title = title, article = article)