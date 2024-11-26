from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<int:article_pk>/', views.article_detail),
    path('articles/<int:article_pk>/comments/', views.comment_create),
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('deposit/<int:deposit_pk>/comments/', views.deposit_comment_create),
    path('saving/<int:saving_pk>/comments/', views.saving_comment_create),
]