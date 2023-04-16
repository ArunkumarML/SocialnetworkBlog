from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from core.models import BlogPost, Comment
from core.backend.serializers import BlogPostSerializer, CommentSerializer
from rest_framework import permissions
from rest_framework.decorators import action


class BlogPostListCreateView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Define a custom action to add likes to a blog post
    @action(detail=True, methods=['post'])
    def add_like(self, request, pk=None):
        # Get the blog post object
        blog_post = self.get_object()

        # Add the current user to the list of users who liked the blog post
        blog_post.likes.add(request.user)

        # Serialize the updated blog post and return the response
        serializer = self.get_serializer(blog_post)
        return Response(serializer.data)


class BlogPostRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CommentRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['get'])
    def get_queryset(self):
        queryset = super().get_queryset()
        blog_post_id = self.kwargs.get('blog_post_pk')
        if blog_post_id:
            queryset = queryset.filter(blog_post__id=blog_post_id).values('')
        return queryset

    @action(detail=True, methods=['post'])
    def create(self, request, *args, **kwargs):
        parent_comment_id = request.data.get('parent_comment_id')
        if parent_comment_id:
            try:
                parent_comment = Comment.objects.get(id=parent_comment_id)
            except Comment.DoesNotExist:
                return Response({'error': 'Parent comment not found'}, status=status.HTTP_400_BAD_REQUEST)
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(author=request.user, parent_comment=parent_comment)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return super().create(request, *args, **kwargs)


class BlogPostLikeAPIView(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Define a custom action to add likes to a blog post
    @action(detail=True, methods=['post'])
    def add_like(self, request, pk=None):
        # Get the blog post object
        blog_post = self.get_object()

        # Add the current user to the list of users who liked the blog post
        blog_post.likes.add(request.user)

        # Serialize the updated blog post and return the response
        serializer = self.get_serializer(blog_post)
        return Response(serializer.data)
