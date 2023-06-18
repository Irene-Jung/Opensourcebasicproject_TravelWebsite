from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
