from django.contrib.auth.models import User
from django.db.models import Count
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from main.models import Like
from ..base_views import BaseApiView
from ..mixins import AuthenticationMixin
from .serializers import LikeAnalyticsSerializer, LikeAnalyticsOutputSerializer, UserActivityAnalyticsSerializer


class LikeAnalytics(AuthenticationMixin, BaseApiView, APIView):
    serializer_class = LikeAnalyticsSerializer
    output_serializer = LikeAnalyticsOutputSerializer

    def get(self, request, *args, **kwargs):
        param_serializer = self.serializer_class(data=request.query_params)

        if not param_serializer.is_valid():
            self.logger.error(f'Input data validation error. Details: {param_serializer.errors}')
            return self.fail(errors=param_serializer.errors)

        date_from = param_serializer.data['date_from']
        date_to = param_serializer.data['date_to']
        qs = Like.objects.filter(
            created_at__range=[date_from, date_to],
        ).values('created_at__date').annotate(total_likes=Count('id'))

        response = self.output_serializer(qs, many=True).data

        return self.success(data=response, status=HTTP_200_OK)


class UserActivityAnalytics(AuthenticationMixin, BaseApiView, APIView):
    output_serializer = UserActivityAnalyticsSerializer

    def get(self, request, *args, **kwargs):
        result = User.objects.prefetch_related('profile') \
            .values('last_login', 'profile__last_activity').get(id=request.user.id)
        response = self.output_serializer(result).data

        return self.success(data=response, status=HTTP_200_OK)
