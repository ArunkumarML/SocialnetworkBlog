from django.urls import path

from core.backend.views import *

comment_view = CommentViewSet.as_view({'get': 'list', 'post': 'create'})
like_view = BlogPostLikeAPIView.as_view({'post': 'add_like'})
urlpatterns = [
    path('blogposts/', BlogPostListCreateView.as_view(), name='blogpost-list-create'),
    path('blogposts/<int:pk>/', BlogPostRetrieveUpdateDeleteView.as_view(), name='blogpost-retrieve-update-delete'),
    path('comments/', comment_view, name='comment-list'),
    path('comments/<int:pk>/', CommentRetrieveUpdateDeleteView.as_view(), name='comment-retrieve-update-delete'),
    path('blogpost/<int:pk>/like/', like_view, name='blogpost-like'),
]
