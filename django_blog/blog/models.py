from django.db import models
from django.conf import settings
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts"
    )

    class Meta:
        ordering = ["-published_date"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.pk)])

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)  # requires Pillow

    def __str__(self):
        return f'Profile of {self.user.username}'

# Automatically create/update profile when User is created
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()