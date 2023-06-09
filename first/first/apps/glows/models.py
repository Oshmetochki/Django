from django.db import models
import datetime
from django.utils import timezone


class Glow(models.Model):
    glow_title=models.CharField('Название статьи',max_length=200)
    glow_text=models.TextField('Текст статьи')
    pub_date=models.DateTimeField('дата публикации')
    def __str__(self):
        return self.glow_title

    def nedavno(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=14))


class Comment(models.Model):
    glow=models.ForeignKey(Glow,on_delete=models.CASCADE)
    author_name=models.CharField('имя автора',max_length=50)
    comment_text=models.CharField('текст комментария',max_length=200)

    def __str__(self):
        return self.author_name