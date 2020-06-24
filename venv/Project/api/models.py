from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=80, help_text="Title of the movie")
    description = models.TextField(max_length=300, help_text="what's on your mind ...")
    category = models.CharField(max_length=50)
    author = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Rating(models.Model):
    Movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    star = models.IntegerField()
    status = models.CharField(max_length=30)
    comments = models.TextField(max_length=300, default="")

    class Meta:
        unique_together = ['Movie', 'star']

    def __str__(self):
        return self.star
