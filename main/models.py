from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.utils import timezone
from django.utils.timezone import now


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    last_activity = models.DateTimeField(default=now)

    def __str__(self):
        return self.user.username


# signals for updating UserProfile after any User changes
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=250, help_text='Post title')
    text = models.TextField(help_text='Post text')
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title[:20]


class Like(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='post_likes', on_delete=models.CASCADE)

    def __str__(self):
        return self.post.title[:20]

    class Meta:
        unique_together = ('post', 'user')
