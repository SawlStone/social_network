from main.models import Post
from api.post.serializers import CreatePostSerializer, LikePostSerializer


class TestCreatePostSerializer:
    serializer_class = CreatePostSerializer

    def test_meta(self):
        serializer_meta = self.serializer_class.Meta

        assert serializer_meta.model is Post
        assert serializer_meta.fields == '__all__'

    def test_create(self, mocker):
        mock_post_obj = mocker.patch.object(Post.objects, 'create')

        self.serializer_class().create(validated_data={
            'title': 'Test title',
            'text': 'Test text',
            'user': 1,
        })

        mock_post_obj.assert_called_once_with(
            title='Test title',
            text='Test text',
            user=1
        )


class TestLikePostSerializer:
    def test_fields(self):
        params = {
            "post_id": 1,
        }
        serializer = LikePostSerializer(params)

        assert serializer.data == params
