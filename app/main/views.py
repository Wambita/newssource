from flask import render_template
from . import main
from ..requests import get_sources, get_articles

@main.route('/')
def index():
    """
        View root page function that returns the index page and its data
    """
    # Getting all sources
    all_sources = get_sources(None)
    title = 'Welcome to The best News site'

    return render_template('index.html', title = title, sources = all_sources)

@main.route('/sources/<category>')
def categories(category):
    """
        View category page function that returns the category page and its data
    """
    all_sources = get_sources(category)
    title = f'All {category} sources'
    return render_template('index.html', title = title, sources = all_sources)


@main.route('/articles/<source>')
def articles(source):
    """
        View articles page function that returns the articles page and its data
    """
    # Getting articles for a specified source
    all_articles = get_articles(source)

    return render_template('articles.html', articles=all_articles)
