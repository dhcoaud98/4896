from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Movie, Review, Genre, ReviewComment
from django.contrib.auth import get_user_model
from .serializers import MovieSerializer, ReviewListSerializer, ReviewCommentSerializer, ReviewSerializer, GenreSerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from datetime import datetime

# 전체 영화 데이터
@api_view(['GET'])
def movies(request):  
    movies = get_list_or_404(Movie)
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

# 장르
@api_view(['GET'])
def genres(request):
    genres = get_list_or_404(Genre)
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)

# 영화 디테일
@api_view(['GET'])
def movie_detail(request, movie_pk):  
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


# 영화 리뷰 작성
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def reviews(request, movie_pk):
    user = request.user
    movie = get_object_or_404(Movie, pk=movie_pk)

    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=user)

        reviews = movie.reviews.all()
        print(reviews)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def review_update_or_delete(request, movie_pk, review_pk):
  movie = get_object_or_404(Movie, pk=movie_pk)
  review = get_object_or_404(Review, pk=review_pk)

  # 로그인 유저일 경우
  # 업데이트
  if request.method == 'PUT':
    
    if request.user == review.user:
        serializer = ReviewSerializer(instance=review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            reviews = movie.reviews.all()
            serializer = ReviewSerializer(reviews, many=True)
            return Response(serializer.data)

  # 삭제
  else:
    if request.user == review.user:
        review.delete()
        reviews = movie.reviews.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)


# 추천 알고리즘
@api_view(['POST'])
def recommend(request): 
    # me_like = request.data.get('me_like')

    movies = get_list_or_404(Movie)
    serializer = MovieSerializer(movies, many=True)
    # pprint(serializer.data)


    ## 1. 런타임이 1시간 이하인 영화 가져오기    
    short_movies = []
    for movie in serializer.data:
        # print(movie['vote_average'])
        # print(movie['runtime'])
        # print(movie['pk'])
        if movie['runtime'] < 60 :
            movie_pick= get_object_or_404(Movie, pk=movie['pk'])
            short_movies.append(movie_pick)
            short_movies_serializer = MovieSerializer(short_movies, many=True)
    
    ## 2. 런타임이 2시간 이상인 영화 가져오기
    long_movies = []
    for movie in serializer.data:
        if movie['runtime'] > 150:
            movie_pick = get_object_or_404(Movie, pk=movie['pk'])
            long_movies.append(movie_pick)
            long_movies_serializer = MovieSerializer(long_movies, many=True)

    ## 3. vote_average가 8점 이상인 영화만 가져오기
    high_vote_movies = []
    for movie in serializer.data:
        if movie['vote_average'] >= 8 :
            movie_pick= get_object_or_404(Movie, pk=movie['pk'])
            high_vote_movies.append(movie_pick)
            high_vote_movies_serializer = MovieSerializer(high_vote_movies, many=True)

    ## 4. 현재 시간과 어울리는 영화 가져오기
    now_time_movies = []
    dt = datetime.now().hour
    # 09 ~ 15 / 액션, 코미디, 다큐, 로맨스, TV영화, 전쟁, 서부, 드라마
    if 9 <= dt < 15 or 21 <= dt <= 23 or 0 <= dt < 5:
        now_genres=[28, 35, 99, 10749, 10770, 10752, 37, 18]
    # 16 ~ 21 / 애니매이션, 모험, 판타지, SF, 음악
    elif 5 <= dt < 9 or 15 <= dt < 21:
        now_genres=[16, 12, 14, 878, 10402]

    for movie in serializer.data:
        if movie['genre'][0] in now_genres:
            movie_pick = get_object_or_404(Movie, pk=movie['pk'])
            now_time_movies.append(movie_pick)
            now_time_movies_serializer = MovieSerializer(now_time_movies, many=True)

    return Response([short_movies_serializer.data, long_movies_serializer.data, high_vote_movies_serializer.data, now_time_movies_serializer.data])


# 영화 좋아요 누르기
@api_view(['POST'])
def like_movie(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user

    if movie.like_users.filter(pk=user.pk).exists():
        movie.like_users.remove(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
      
    else:
        movie.like_users.add(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
      

# 영화를 좋아요한 유저목록
@api_view(['POST'])
def like_movie_users(request, my_pk):  
  # print(request.data)
  users = []
  movies = request.data.get('movies')

  for movie in movies:
    movie = get_object_or_404(Movie, pk=movie)
    serializer = MovieSerializer(movie)

    for user in serializer.data.get('like_users'):
      if user not in users:
        users.append(user)
    
  return Response(users)

  