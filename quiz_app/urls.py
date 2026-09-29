from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('start/', views.start_quiz, name='start_quiz'),
    path('quiz/<int:category_id>/', views.quiz, name='quiz'),
    path('quiz/<int:category_id>/submit/', views.submit_quiz, name='submit_quiz'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
]
