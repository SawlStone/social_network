from rest_framework.status import HTTP_201_CREATED
from rest_framework.views import APIView
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework_jwt.views import ObtainJSONWebToken

from .serializers import CreateUserSerializer
from ..base_views import BaseApiView


class CreateUserApiView(BaseApiView, APIView):
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            self.logger.error(f'Input data validation error. Details: {serializer.errors}')
            return self.fail(errors=serializer.errors)

        serializer.save()
        output = serializer.data
        output.pop('password')
        self.logger.debug(f'Post was created. Details: {output}')
        return self.success(data=output, status=HTTP_201_CREATED)


class LoginUserApiView(BaseApiView, ObtainJSONWebToken):
    serializer_class = JSONWebTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            self.logger.error(f'Input data validation error. Details: {serializer.errors}')
            return self.fail(errors=serializer.errors)

        username = serializer.object['user'].username
        response = {
            'user': username,
            'token': serializer.object['token']
        }
        self.logger.debug(f'Token was create for. Details: {username}')

        return self.success(data=response, status=HTTP_201_CREATED)
