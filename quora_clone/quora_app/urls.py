from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('post_question/', views.post_question, name='post_question'),
    path('questions/', views.view_questions, name='view_questions'),
    path('post_answer/<int:question_id>/', views.post_answer, name='post_answer'),
    path('like_answer/<int:answer_id>/', views.like_answer, name='like_answer'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]


