from datetime import date, datetime

from api.analytics.serializers import LikeAnalyticsSerializer, LikeAnalyticsOutputSerializer, \
    UserActivityAnalyticsSerializer


class TestLikeAnalyticsSerializer:
    def test_fields(self):
        params = {
            "date_from": "2020-06-02",
            "date_to": "2020-06-02"
        }
        serializer = LikeAnalyticsSerializer(params)

        assert serializer.data == params


class TestLikeAnalyticsOutputSerializer:
    def test_fields(self):
        params = {
            "created_at__date": date(2020, 6, 2),
            "total_likes": 4,
        }
        serializer = LikeAnalyticsOutputSerializer(params)

        assert serializer.data == {
            "data": "2020-06-02",
            "total_likes": 4,
        }


class TestUserActivityAnalyticsSerializer:
    params = {
        "last_login": datetime(2020, 6, 2, 10, 10, 10),
        "profile__last_activity": datetime(2020, 6, 3, 11, 11, 11),
    }
    serializer = UserActivityAnalyticsSerializer(params)

    assert serializer.data == {
        "last_login": "2020-06-02T10:10:10Z",
        "last_activity": "2020-06-03T11:11:11Z",
    }
