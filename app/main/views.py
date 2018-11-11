from flask import render_template
from . import main
# from ..requests import get_sources

@main.route('/')
def index():
    """
        View root page function that returns the index page and its data
    """
    title = 'Welcome to The best News site'

    return render_template('index.html', title = title)
