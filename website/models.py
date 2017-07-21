from django.conf import settings
from django.db import models


class Article(models.Model):
    '''Holds information for an article

    content: the content of the article
    publish_date_time: the date and time the article was posted
    author: the User who wrote the article
    '''

    content = models.TextField()
    publish_date_time = models.DateTimeField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL)

    # In the future, we might consider adding an image to each article for prettier displays
    # image = models.ImageField()
