from .models import Source, Article
from newsapi import NewsApiClient

# Getting the api key
api_key = None

newsapi = None

def configure_request(app):
    """
        Function that retrives the api key and base url from the config file

        Args:
        app: The flask app instance
    """
    global api_key, newsapi
    api_key = app.config['NEWS_API_KEY']
    newsapi = NewsApiClient(api_key = api_key)
    
def get_sources(category):
    """
       Functions that gets all the sources 
    """
    sources = newsapi.get_sources(category=category)

    results = None

    if sources['status'] == 'ok':
        sources_list = sources['sources']
        results = process_results(sources_list)

    return results

def get_articles(source):
    """
        Function that get all articles for a specified source.
    """
    all_articles = newsapi.get_everything(sources=source)

    results = []

    if all_articles['status'] == 'ok':
        articles_list = all_articles['articles']
        for article in articles_list:
            author = article.get('author')
            title = article.get('title')
            image = article.get('urlToImage')
            description = article.get('description')
            time = article.get('publishedAt')[0:10]
            url = article.get('url')

            if image:
                article_object = Article(author, title, image, description, time, url)
                results.append(article_object)

    return results


    
def process_results(sources_list):
    """
        Function that processes the sources list and transform them to a list of Objects

      Args:
        sources_list: A list of dictionaries that contain news source details

      Returns:
        A list of source objects
    """
    sources_results = []
    for source in sources_list:
        id = source.get('id')
        name = source.get('name')
        category = source.get('category')
        description = source.get('description')

        source_object = Source(id, name, category, description)
        sources_results.append(source_object)

    return sources_results
