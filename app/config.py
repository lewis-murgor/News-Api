class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_URL = 'https://newsapi.org/v2/top-headlines/sources?apiKey={}'
    ARTICLES_API_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    SEARCH_API_URL = 'https://newsapi.org/v2/everything?q={}&apiKey={}'



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True