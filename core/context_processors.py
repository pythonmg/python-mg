from django.contrib.auth.models import User
from twitter_app.models import Tweet


def tweets(request):
    return {
        'tweets': Tweet.objects.filter().order_by('-created_at')[:5]
    }


def members(request):
    return {
        'members': User.objects.filter(is_superuser=False).order_by('?')[:12]
    }
