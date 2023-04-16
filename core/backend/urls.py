from django.urls import path

from core.backend.views import *

comment_view = CommentViewSet.as_view({'get': 'list', 'post': 'create'})
urlpatterns = [
    path('blogposts/', BlogPostListCreateView.as_view(), name='blogpost-list-create'),
    path('blogposts/<int:pk>/', BlogPostRetrieveUpdateDeleteView.as_view(), name='blogpost-retrieve-update-delete'),
    path('comments/', comment_view, name='comment-list'),
    path('comments/<int:pk>/', CommentRetrieveUpdateDeleteView.as_view(), name='comment-retrieve-update-delete'),
]
