from collections import namedtuple


MeetupSocial = namedtuple('MeetupSocial', ['name', 'identifier'])

def parse_social(data):
    social = []
    for key, value in data.items():
        social.append(MeetupSocial(name=key, identifier=value.get('identifier')))
    return social

MeetupPhoto = namedtuple('MeetupPhoto', ['guid', 'photo_link', 'highres_link', 'thumb_link'])

def parse_photo(data):
    if not data:
        return None
    return MeetupPhoto(
        guid=data.get('photo_id', None),
        photo_link=data.get('photo_link', None),
        highres_link=data.get('highres_link', None),
        thumb_link=data.get('thumb_link', None)
    )

MeetupMember = namedtuple('MeetupMember', ['guid', 'name', 'social', 'photo', 'link'])

def parse_member(data):
    return MeetupMember(
        guid=data.get('id', None),
        name=data.get('name', None),
        social=parse_social(data.get('other_services')),
        photo=parse_photo(data.get('photo', None)),
        link=data.get('link')
    )
