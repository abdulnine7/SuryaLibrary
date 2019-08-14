from django.db import models
from django.utils import timezone
from users.models import User, Area

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    isbn_no = models.CharField(max_length=100, null=True, blank=True)
    pages = models.IntegerField(null=True, blank=True)
    language = models.CharField(max_length=100, null=True, blank=True)
    available_copies = models.IntegerField()
    total_copies = models.IntegerField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Review(models.Model):
    STAR = ( (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), )
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=STAR)
    description = models.TextField(null=True, blank=True)
    admin_confirmed = models.BooleanField()

    def __str__(self):
        text = self.book.title + " ( "
        for x in range(0, self.rating):
            text += "*"
        text += " ) - " + self.description
        return text

class Delivery(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    message = models.CharField(max_length=200, default="NO REMARKS")
    deliverd = models.BooleanField(default =False)

    def __str__(self):
        return "Deliver '" + self.book.title +"' to " + self.user.username + " in " + self.area.name
