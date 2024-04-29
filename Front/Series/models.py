from django.db import models
import datetime

class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    director = models.CharField(max_length=255)
    description = models.TextField()
    poster = models.ImageField(upload_to='movie_posters/')
    video_file = models.FileField(upload_to='movie_files/')
    duration_minutes = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class TVSerie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    director = models.ForeignKey('Director', on_delete=models.CASCADE)
    genres = models.ManyToManyField('Genre')
    poster = models.ImageField(upload_to='tv_series_posters/')
    num_seasons = models.PositiveIntegerField()
    num_episodes = models.PositiveIntegerField()
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.title

class Season(models.Model):
    series = models.ForeignKey(TVSeries, on_delete=models.CASCADE)
    number = models.PositiveIntegerField()
    release_date = models.DateField()
    poster = models.ImageField(upload_to='season_posters/')

    class Meta:
        unique_together = ('series', 'number')

    def __str__(self):
        return f"{self.series.title} - Season {self.number}"

class Episode(models.Model):
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    video_url = models.URLField()

    def __str__(self):
        return f"{self.season.series.title} - S{self.season.number}E{self.number}: {self.title}"


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
