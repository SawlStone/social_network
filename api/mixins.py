import logging

from rest_framework import permissions
from rest_framework.response import Response


class LoggerMixin(object):
    @property
    def logger(self):
        name = '.'.join([__name__, self.__class__.__name__])
        return logging.getLogger(name)


class APIMixin(object):
    def success(self, data=None, status=None):
        if data is None:
            return Response(data={
                'status': 'OK',
            }, status=status)
        return Response(data={
            'status': 'OK',
            'data': data
        }, status=status)

    def fail(self, errors, status=400):
        return Response(data={
            'status': 'FAIL',
            'errors': errors,
        }, status=status)


class AuthenticationMixin(object):
    permission_classes = (permissions.IsAuthenticated,)
