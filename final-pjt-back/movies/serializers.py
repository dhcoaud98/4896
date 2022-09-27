from rest_framework import serializers
from django.contrib.auth import get_user_model
from articles.serializers.article import User
from .models import Genre, Movie, Review, ReviewComment

User = get_user_model()

# MovieList
class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

# GenreList
class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'
        

# Review
class ReviewSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    user = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ('pk', 'user', 'content', 'movie','rank',)
        read_only_fields = ('movie','rank','title',)


# Movie
class MovieSerializer(serializers.ModelSerializer):

    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('pk', 'title', 'overview', 'poster_path', 'vote_average', 'release_date', 'runtime', 'popularity', 'genre', 'adult', 'reviews','like_users' )
        read_only_fields = ('like_users',)


# ReviewList
class ReviewListSerializer(serializers.ModelSerializer):
  movie_title = serializers.SerializerMethodField()
  username = serializers.SerializerMethodField()
  
  def get_movie_title(self, obj):
    return obj.movie.title
  
  def get_username(self, obj):
    return obj.user.username

  class Meta:
    model = Review
    fields = ('id', 'user', 'username', 'title', 'content', 'movie_id', 'movie_title', 'rank', 'created_at', 'updated_at',)
    read_only_fields = ('user',)


# ReviewComment
class ReviewCommentSerializer(serializers.ModelSerializer):
  username = serializers.SerializerMethodField()
  
  def get_username(self,obj):
    return obj.user.username

  class Meta:
    model = ReviewComment
    fields = ('id', 'user', 'username', 'user', 'content', 'review', 'created_at', 'updated_at',)
    read_only_fields = ('user', 'review',)