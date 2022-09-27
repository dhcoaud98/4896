from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    poster_path = models.TextField()
    vote_average = models.FloatField()
    release_date = models.TextField()
    runtime = models.IntegerField()
    popularity = models.FloatField(validators=[MinValueValidator(0)])  # 영화 선호도
    genre = models.ManyToManyField(Genre) 
    adult = models.BooleanField()  # user에서 나이를 입력 받은 후 관람할 수 있는 영화인지?
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')  # 영화 좋아요 기능
 

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    rank = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)], null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews")
    

class ReviewComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="review_comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)