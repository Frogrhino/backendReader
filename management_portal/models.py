from django.db import models


class Manga(models.Model):
    name = models.CharField(max_length=200)
    rating = models.FloatField(default=0)
    alternate_titles = models.TextField(null=True)
    description = models.TextField(null=True)
    status = models.CharField(null=True, max_length=20)
    author = models.CharField(null=True, max_length=50)
    artist = models.CharField(null=True, max_length=50)
    created_on = models.DateField(null=True)
    posted_on = models.DateTimeField(null=True)
    updated_on = models.DateTimeField(null=True)
    keywords = models.TextField(null=True)

    def __repr__(self) -> str:
        return super().__repr__()

    def __str__(self) -> str:
        return super().__str__()
