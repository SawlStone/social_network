from django.contrib.auth.models import User
from api.auth.serializers import CreateUserSerializer


class TestCreateUserSerializer:
    serializer_class = CreateUserSerializer

    def test_meta(self):
        serializer_meta = self.serializer_class.Meta

        assert serializer_meta.model is User
        assert serializer_meta.fields == ('username', 'password', 'email', )

    def test_create(self, mocker):
        mock_user = mocker.patch.object(User.objects, 'create_user')

        self.serializer_class().create(validated_data={
            'email': 'admin@gmail.com',
            'username': 'admin',
            'password': '12345',
        })

        mock_user.assert_called_once_with(
            email='admin@gmail.com',
            username='admin',
            password='12345',
        )
