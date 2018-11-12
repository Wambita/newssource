# import urllib.request, json
from .models import Source
from newsapi import NewsApiClient

# Getting the movie base url
# base_url = None

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
    # base_url = app.config['NEWS_API_BASE_URL']
    api_key = app.config['NEWS_API_KEY']
    newsapi = NewsApiClient(api_key = api_key)
    
def get_sources():
    """
       Functions that gets all the sources 
    """
    sources = newsapi.get_sources()

    results = None

    if sources['status'] == 'ok':
        sources_list = sources['sources']
        results = process_results(sources_list)

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
        description = source.get('description')

        source_object = Source(id, name, description)
        sources_results.append(source_object)

    return sources_results
