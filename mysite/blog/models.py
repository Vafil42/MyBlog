from django.db import models
from django.utils import timezone

class Article(models.Model):
    article_name = models.CharField(max_length=30)
    article_text = models.TextField()
    article_date = models.DateTimeField('date published')
    def __str__(self):
        return self.article_name

class Comment(models.Model):
    comment_author = models.CharField(max_length=30)
    comment_text = models.TextField()
    comment_date = models.DateTimeField()
    comment_article_id = models.IntegerField()
    def __str__(self):
        return self.comment_text
