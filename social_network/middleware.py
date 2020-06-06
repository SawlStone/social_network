from django.utils import timezone

from main.models import UserProfile


class UpdateLastActivityMiddleware(object):
    """
        Updating last activity once in minute, not to overload the database
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            now = timezone.now()
            user_profile = UserProfile.objects.get(user__id=request.user.id)
            difference = now - user_profile.last_activity
            if difference.seconds > 60:
                user_profile.last_activity = now
                user_profile.save()
        response = self.get_response(request)
        return response
