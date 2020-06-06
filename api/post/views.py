from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_503_SERVICE_UNAVAILABLE
from rest_framework.views import APIView

from main.models import Like
from ..base_views import BaseApiView
from ..mixins import AuthenticationMixin
from .serializers import CreatePostSerializer, LikePostSerializer


class CreatePostApiView(AuthenticationMixin, BaseApiView,  APIView):
    serializer_class = CreatePostSerializer

    def post(self, request, *args, **kwargs):
        request.data['user'] = request.user.id
        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            self.logger.error(f'Input data validation error. Details: {serializer.errors}')
            return self.fail(errors=serializer.errors)

        serializer.save()
        self.logger.debug(f'Post was created. Details: {serializer.data}')

        return self.success(data=serializer.data, status=HTTP_201_CREATED)


class LikePostApiView(AuthenticationMixin, BaseApiView,  APIView):
    serializer_class = LikePostSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            self.logger.error(f'Input data validation error. Details: {serializer.errors}')
            return self.fail(errors=serializer.errors)

        post_id = serializer.data['post_id']
        user = request.user

        try:
            like_obj, created = Like.objects.get_or_create(post_id=post_id, user_id=user.id)
        except Exception as ex:
            self.logger.error(f'DB error. Details: {ex}')
            return self.fail(
                errors={'db_error': 'SERVICE_UNAVAILABLE'},
                status=HTTP_503_SERVICE_UNAVAILABLE
            )

        like = True
        if not created:
            like_obj.delete()
            like = False
        response = {
            "post_id": post_id,
            "like": like,
        }
        self.logger.debug(f'Post was liked. Details: {response}')

        return self.success(data=response, status=HTTP_200_OK)
