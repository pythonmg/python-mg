from django.conf import settings
import json
import mimeparse
import requests
import urllib

from .parsers import parse_member
from .exceptions import (
    MeetupsNotJson, MeetupsBadJson, MeetupsMeetupDown, MeetupsBadResponse,
    MeetupsRateLimitExceeded
)


MEETUP_API_HOST = 'https://api.meetup.com'
MEMBERS_URL = MEETUP_API_HOST + '/2/members'
GROUP_URLNAME = settings.MEETUP_GROUP_URLNAME


class Meetup(object):

    def __init__(self, http_timeout=30, http_retries=2):
        self._api_key = settings.MEETUP_API_KEY
        self._http_timeout = http_timeout
        self._http_retries = http_retries

    def members(self):
        query = urllib.urlencode({'key': self._api_key,
                                  'group_urlname': GROUP_URLNAME})
        url = '{0}?{1}'.format(MEMBERS_URL, query)
        data = self._http_get_json(url)
        members = data['results']
        return [parse_member(member) for member in members]

    def _http_get_json(self, url):
        response = self._http_get(url)

        content_type = response.headers['content-type']
        parsed_mimetype = mimeparse.parse_mime_type(content_type)
        if parsed_mimetype[1] not in ('json', 'javascript'):
            raise MeetupsNotJson(content_type)

        try:
            return json.loads(response.content)
        except ValueError as e:
            raise MeetupsBadJson(e)

    def _http_get(self, url):
        for try_number in range(self._http_retries + 1):
            response = requests.get(url, timeout=self._http_timeout)
            if response.status_code == 200:
                return response

            if (try_number >= self._http_retries or
                    response.status_code not in (408, 500, 502, 503, 504)):

                if response.status_code >= 500:
                    raise MeetupsMeetupDown(response, response.content)
                if response.status_code == 400:
                    try:
                        data = json.loads(response.content)
                        if data.get('code', None) == 'limit':
                            raise MeetupsRateLimitExceeded
                    except:  # Don't lose original error when JSON is bad
                        pass
                raise MeetupsBadResponse(response, response.content)
