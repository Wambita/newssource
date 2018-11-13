class Source:
    """
        Source class that defines a news source objects.
    """
    def __init__(self, id, name, category, description):
        """
            Function that creates instances of the source objects.
        """
        self.id = id
        self.name = name
        self.category = category
        self.description = description

class Article:
    """
        Article class that defines article objects.
    """
    def __init__(self, author, title, image, description, time, url ):
        """
            Function that creates instances of the article objects.
        """
        self.author = author
        self.title = title
        self.image = image
        self.description = description
        self.time = time
        self.url = url