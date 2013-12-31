import webapp2
import settings
import meetup_api.api as meetupapi

from datetime import datetime
from utils import utils
from google.appengine.ext import ndb
from meetup_api.models import MeetupGroup
from meetup_api.models import MeetupEvent
from meetup_api.models import MeetupLocation
from meetup_api.models import MeetupMember


class RefreshDb(webapp2.RequestHandler):
    """ Gets all of the content that is related to an API and then updates
    those that are already in the DB if necessary.
    """
    def get(self):
        api = meetupapi.MeetupApi()
        events = api.getAllObjects(model='events',group_urlname='GDG-SP',\
            status="past,upcoming")
        groups = api.getAllObjects(model='groups',group_urlname='GDG-SP')

        eventInstances = list()
        locationInstances = list()
        groupInstances = list()

        for grupo in groups:
            query = MeetupGroup.\
                query(MeetupGroup.group_id == str(grupo.id)).iter()
            if query.has_next():
                meetupGroup = query.next()
            else:
                meetupGroup = MeetupGroup(\
                    parent=ndb.Key('MeetupGroup',grupo.urlname))
            meetupGroup.group_id = grupo.id
            meetupGroup = utils.injectAttrsExpando(grupo,meetupGroup)
            meetupGroup.put()

        for evento in events:
            query = MeetupEvent.\
                query(MeetupEvent.event_id == evento.id).iter()
            if query.has_next():
                meetupEvent = query.next()
            else:
                meetupEvent = MeetupEvent(\
                    parent=ndb.Key('MeetupEvent',evento.group['urlname']))

            time = datetime.fromtimestamp(\
                                float(evento.time)/1000.0)
            updated = datetime.fromtimestamp(\
                                float(evento.updated)/1000.0)

            if evento.duration == None:
                duration = 0
            else:
                duration = int(evento.duration)

            grupo = MeetupGroup.query(\
                MeetupGroup.group_id == str(evento.group['id'])).iter()
            try:
                grupo = grupo.next()
                meetupEvent.group           = grupo.key
            except StopIteration:
                grupo = None

            meetupEvent.event_id        = evento.id
            meetupEvent.name            = evento.name
            meetupEvent.time            = time
            meetupEvent.description     = evento.description
            meetupEvent.duration        = duration
            meetupEvent.event_url       = evento.event_url
            meetupEvent.maybe_rsvp_count= int(evento.maybe_rsvp_count)
            meetupEvent.yes_rsvp_count  = int(evento.yes_rsvp_count)
            meetupEvent.photo_url       = evento.photo_url
            meetupEvent.status          = evento.status
            meetupEvent.updated         = updated
            meetupEvent.put()

            if getattr(evento,'venue',None) != None:
                venue_id = str(evento.venue['id'])

                qry = MeetupLocation.query(\
                        MeetupLocation.venue_id == venue_id).iter()
                if qry.has_next():
                    meetupLocation = qry.next()
                else:
                    meetupLocation = MeetupLocation(parent=ndb.Key(\
                        'MeetupLocation',evento.name))

                meetupLocation.address_1    = evento.venue['address_1']
                meetupLocation.venue_id     = venue_id
                meetupLocation.lat_lon      = \
                    ndb.GeoPt(float(evento.venue['lat']),\
                                float(evento.venue['lon']))
                meetupLocation.name         = evento.venue['name']
                meetupLocation.event        = meetupEvent.key
                meetupLocation.put()

def getMemberKey(name):
    return ndb.Key('MeetupMember',name)
