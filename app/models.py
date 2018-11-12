class Source:
    """
        Source class that defines a news source objects.
    """
    def __init__(self, id, name, description):
        """
            Function that creates instances of the source objects.
        """
        self.id = id
        self.name = name
        self.description = description

class Article:
    """
        Article class that defines article objects.
    """
    def __init__(self, title, image, description, time, url ):
        """
            Function that creates instances of the article objects.
        """
        self.title = title
        self.image = image
        self.description = description
        self.time = time
        self.url = url