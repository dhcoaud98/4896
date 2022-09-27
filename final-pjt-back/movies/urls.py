from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    # movies
    path('', views.movies),
    path('genres/', views.genres),
    path('<int:movie_pk>/', views.movie_detail),  # 영화 디테일
    
    # reviews
    path('<int:movie_pk>/reviews/', views.reviews),  # 영화 리뷰
    path('<int:movie_pk>/reviews/<int:review_pk>/', views.review_update_or_delete),
    
    path('recommend/', views.recommend),
    path('<int:movie_pk>/like/', views.like_movie),  # 영화 좋아요

    path('<int:my_pk>/like/users/', views.like_movie_users),
]
