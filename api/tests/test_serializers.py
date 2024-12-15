import pytest
from api.serializers import PostSerializer, PostUpdateSerializer
from api.tests.factories import PostFactory


@pytest.mark.django_db
class TestPostSerializer:

    def test_valid_post_creation(self):
        data = {
            "username": "username",
            "title": "Test Title",
            "content": "This is a test content.",
        }
        serializer = PostSerializer(data=data)

        assert serializer.is_valid()
        validated_data = serializer.validated_data
        assert validated_data["username"] == data["username"]

    def test_username_required_on_create(self):
        data = {
            "title": "Test Title",
            "content": "This is a test content.",
        }
        serializer = PostSerializer(data=data)

        assert not serializer.is_valid()
        assert "username" in serializer.errors
        assert serializer.errors["username"] == ["This field is required."]

    def test_username_will_not_be_updated(self):
        post = PostFactory(username="initial_user")
        data = {
            "username": "updated_user",
            "title": post.title,
            "content": post.content,
        }
        serializer = PostUpdateSerializer(post, data=data, partial=True)

        assert serializer.is_valid()
        assert post.username == 'initial_user'

    def test_partial_update_without_username(self):
        post = PostFactory(username="initial_user")
        data = {
            "title": "Updated Title",
        }
        serializer = PostSerializer(post, data=data, partial=True)

        assert serializer.is_valid()
        validated_data = serializer.validated_data
        assert validated_data["title"] == data["title"]
