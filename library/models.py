from django.db import models
from django.utils import timezone

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    isbn_no = models.CharField(max_length=100, null=True, blank=True)
    pages = models.IntegerField(null=True, blank=True)
    language = models.CharField(max_length=100, null=True, blank=True)
    available_copies = models.IntegerField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    admin_confirmed = models.BooleanField()

    def __str__(self):
        text = self.item.title + " ( "
        for x in range(0, self.rating):
            text += "*"
        text += " ) - " + self.description
        return text
