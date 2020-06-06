from rest_framework import serializers


class LikeAnalyticsSerializer(serializers.Serializer):
    date_from = serializers.DateField()
    date_to = serializers.DateField()


class LikeAnalyticsOutputSerializer(serializers.Serializer):
    data = serializers.DateField(source='created_at__date')
    total_likes = serializers.IntegerField()


class UserActivityAnalyticsSerializer(serializers.Serializer):
    # TODO: add datetime format if needed
    last_login = serializers.DateTimeField()
    last_activity = serializers.DateTimeField(source='profile__last_activity')
