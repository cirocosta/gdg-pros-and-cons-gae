import webapp2
import settings
import meetup_api.api as meetupapi

from google.appengine.ext import ndb
from meetup_api.models import MeetupGroup,MeetupMember,MeetupEvent


class RefreshDb(webapp2.RequestHandler):
    """ Gets all of the content that is related to an API and then updates
    those that are already in the DB if necessary.
    """
    def get(self):
        api = meetupapi.MeetupApi()
        events = api.getAllObjects(model='events',group_urlname='GDG-SP')
        groups = api.getAllObjects(model='groups',group_urlname='GDG-SP')

        for evento in events:
            query = MeetupEvent.\
                query(MeetupEvent.event_id == evento.id).iter()
            if query.has_next():
                meetupEvent = query.next()
            else:
                meetupEvent = MeetupEvent(\
                    parent=ndb.Key('MeetupEvent',evento.group['urlname']))
            print meetupEvent

        for grupo in groups:
            query = MeetupGroup.\
                query(MeetupGroup.group_id == grupo.id).iter()
            if query.has_next():
                meetupGroup = query.next()
            else:
                meetupGroup = MeetupGroup(\
                    parent=ndb.Key('MeetupGroup',grupo.urlname))
            print meetupGroup

def getMemberKey(name):
    return ndb.Key('MeetupMember',name)

# api = meetupapi.MeetupApi(api_key=settings.MEETUP_API_KEY)
# for obj in api.getObject(model='groups',group_urlname='GDG-SP'):
#     print obj.__dict__
