
from flask import render_template
from app import app
from .request import get_news_sources

@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    news = get_news_sources()
    title = 'News Sources'
    return render_template('index.html', title = title, news = news)

@app.route('/article/<article_id>')
def article(article_id):
    '''
    View article page function that returns the news articles page and its details
    '''
    title = 'News Articles'
    return render_template('article.html', id = article_id, title = title)