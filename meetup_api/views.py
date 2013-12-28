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
        get_event(0)
        get_group(settings.MEETUP_GDG_GROUP_ID)
        self.response.write('done!')

def get_event(event_id):
    pass

def get_group(group_id):
    api = meetupapi.MeetupApi(api_key=settings.MEETUP_API_KEY)
    pass

def getMemberKey(name):
    return ndb.Key('MeetupMember',name)


# api = meetupapi.MeetupApi(api_key=settings.MEETUP_API_KEY)
# for obj in api.getObject(model='groups',group_urlname='GDG-SP'):
#     print obj.__dict__
