from meetup.models import Member
from twitter_app.models import Tweet


def tweets(request):
    return {
        'tweets': Tweet.objects.filter().order_by('-created_at')[:5]
    }


def members(request):
    return {
        'members': Member.objects.order_by('?')[:12]
    }
