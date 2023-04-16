from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from .models import BlogPost, Comment, User


class BlogPostTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.blog_post = BlogPost.objects.create(title='Test Blog Post', content='Test Content',
                                                 author=User.objects.create_superuser(email='test@gmail.com',
                                                                                      password='test@123'))

    def test_get_blog_posts(self):
        # Test getting a list of blog posts
        response = self.client.get(reverse('blogpost-list-create'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_blog_post(self):
        # Test creating a new blog post
        data = {'title': 'New Blog Post', 'content': 'New Content'}
        response = self.client.post(reverse('blogpost-list-create'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(BlogPost.objects.count(), 2)

    def test_get_blog_post_detail(self):
        # Test getting detail of a blog post
        response = self.client.get(reverse('blogpost-retrieve-update-delete', args=[self.blog_post.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Blog Post')

    def test_update_blog_post(self):
        # Test updating a blog post
        data = {'title': 'Updated Blog Post', 'content': 'Updated Content'}
        response = self.client.put(reverse('blogpost-retrieve-update-delete', args=[self.blog_post.id]), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.blog_post.refresh_from_db()
        self.assertEqual(self.blog_post.title, 'Updated Blog Post')

    def test_delete_blog_post(self):
        # Test deleting a blog post
        response = self.client.delete(reverse('blogpost-retrieve-update-delete', args=[self.blog_post.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(BlogPost.objects.count(), 0)


class CommentTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        author = User.objects.create_superuser(email='test2@gmail.com', password='test@123')
        self.blog_post = BlogPost.objects.create(title='Test Blog Post', content='Test Content',
                                                 author=author)
        self.comment = Comment.objects.create(post=self.blog_post,
                                              author=author,
                                              content='Test Comment')

    def test_get_comment(self):
        # Test getting a comment
        author = User.objects.get(email='test2@gmail.com', password='test@123')
        response = self.client.get(reverse('comment-retrieve-update-delete', args=[self.comment.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['author'], author.id)

    def test_update_comment(self):
        # Test updating a comment
        data = {'content': 'Updated Comment'}
        response = self.client.put(reverse('comment-retrieve-update-delete', args=[self.comment.id]), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.comment.refresh_from_db()
        self.assertEqual(self.comment.content, 'Updated Comment')

    def test_delete_comment(self):
        # Test deleting a comment
        response = self.client.delete(reverse('comment-retrieve-update-delete', args=[self.comment.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Comment.objects.count(), 0)
