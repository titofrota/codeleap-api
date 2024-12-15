# tests for views.py
import pytest
from rest_framework import status
from rest_framework.test import APIClient
from api.models import Post
from api.tests.factories import PostFactory
from dateutil.parser import isoparse


@pytest.mark.django_db
class TestPostViewSet:

    def setup_method(self):
        self.client = APIClient()

    def test_create_post(self):
        data = {
            "username": "johndoe",
            "title": "Test Title",
            "content": "Test Content"
        }

        response = self.client.post("/api/v1/posts/", data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['username'] == data['username']
        assert response.data['title'] == data['title']
        assert response.data['content'] == data['content']

    def test_create_post_without_title(self):
        data = {
            "username": "johndoe",
            "content": "Test Content"
        }

        response = self.client.post("/api/v1/posts/", data, format='json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "title" in response.data
        assert response.data["title"] == ["This field is required."]

    def test_create_post_without_username(self):
        data = {
            "title": "Test Title",
            "content": "Test Content"
        }

        response = self.client.post("/api/v1/posts/", data, format='json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert "username" in response.data
        assert response.data["username"] == ["This field is required."]

    def test_valid_update_post(self):
        post = PostFactory()
        data = {
            "title": "Updated Title",
            "content": "Updated Content"
        }

        response = self.client.patch(f"/api/v1/posts/{post.id}/", data, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['title'] == data['title']
        assert response.data['content'] == data['content']

    def test_username_will_not_be_updated(self):
        post = PostFactory(username="initial_user")
        data = {
            "username": "updated_user",
            "title": post.title,
            "content": post.content,
        }

        response = self.client.patch(f"/api/v1/posts/{post.id}/", data, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert post.username == 'initial_user'

    def test_get_post_by_id(self):
        post = PostFactory()
        response = self.client.get(f"/api/v1/posts/{post.id}/")

        assert response.status_code == status.HTTP_200_OK
        assert response.data['username'] == post.username
        assert response.data['title'] == post.title
        assert response.data['content'] == post.content
        assert isoparse(response.data['created_datetime']) == post.created_datetime
        assert response.data['id'] == post.id

    def test_get_post_by_id_not_found(self):
        response = self.client.get("/api/v1/posts/99999/")

        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_get_all_posts(self):
        PostFactory.create_batch(5)
        response = self.client.get("/api/v1/posts/")

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 5

    def test_delete_post(self):
        post = PostFactory()
        response = self.client.delete(f"/api/v1/posts/{post.id}/")

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert not Post.objects.filter(id=post.id).exists()

    def test_delete_post_not_found(self):
        response = self.client.delete("/api/v1/posts/99999/")

        assert response.status_code == status.HTTP_404_NOT_FOUND
