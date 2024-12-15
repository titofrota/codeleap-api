import pytest
from api.models import Post
from datetime import datetime


@pytest.mark.django_db
class TestPostModel:

    def test_create_post_successful(self):
        post = Post.objects.create(
            username="johndoe",
            title="Test Title",
            content="Test Content"
        )
        assert post.id is not None
        assert post.username == "johndoe"
        assert post.title == "Test Title"
        assert post.content == "Test Content"
        assert isinstance(post.created_datetime, datetime)

    def test_post_str_method(self):
        post = Post.objects.create(
            username="johndoe",
            title="Test Title",
            content="Test Content"
        )

        assert str(post) == "Test Title"

    def test_created_datetime_auto_set(self):
        post = Post.objects.create(
            username="johndoe",
            title="Test Title",
            content="Test Content"
        )

        assert post.created_datetime is not None
