from django.urls import path

from api.analytics.views import LikeAnalytics, UserActivityAnalytics
from api.post.views import CreatePostApiView, LikePostApiView
from api.auth.views import CreateUserApiView, LoginUserApiView


urlpatterns = [
    path('auth/user/signup/', CreateUserApiView.as_view(), name='signup_user'),
    path('auth/user/login/', LoginUserApiView.as_view(), name='login_user'),

    path('post/create/', CreatePostApiView.as_view(), name='create_post'),
    path('post/like/', LikePostApiView.as_view(), name='like_post'),

    path('analytics/like/', LikeAnalytics.as_view(), name='analytics_like'),
    path('analytics/user_activity/', UserActivityAnalytics.as_view(), name='analytics_user_activity'),
]
