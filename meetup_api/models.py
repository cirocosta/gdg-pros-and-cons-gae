# Models to store the data comming from Meetup API. This will reflect
# a bit of the same state of the responses from the reffered API.

import endpoints

from google.appengine.ext import ndb
from protorpc import remote
from endpoints_proto_datastore.ndb import EndpointsModel
from datetime import datetime
from votescreen.models import Comment


class MeetupGroup(EndpointsModel):
    """ Utilizing ndb.Expando to show how easy it is to use this with
    the model of API that we've built. """

    _message_fields_schema = (
        'id','group_id','name','description','urlname','members',
        )

    group_id    = ndb.StringProperty(indexed=True,required=True)
    name        = ndb.StringProperty(indexed=True)
    description = ndb.StringProperty(indexed=False)
    urlname     = ndb.StringProperty(indexed=True)
    members     = ndb.IntegerProperty()


class MeetupEvent(EndpointsModel):
    event_id            = ndb.StringProperty(indexed=True,required=True)
    name                = ndb.StringProperty(indexed=True)
    time                = ndb.DateTimeProperty(indexed=True)
    description         = ndb.StringProperty(indexed=False)
    duration            = ndb.IntegerProperty()
    event_url           = ndb.StringProperty()
    maybe_rsvp_count    = ndb.IntegerProperty()
    yes_rsvp_count      = ndb.IntegerProperty()
    photo_url           = ndb.StringProperty()
    status              = ndb.StringProperty(indexed=True)
    updated             = ndb.DateTimeProperty(indexed=True)
    group               = ndb.KeyProperty(kind=MeetupGroup)

    @classmethod
    def getGroupEvents(cls,group_key):
        """ Returns the current or the next event that we'll have """
        #TODO : resolve the case where we have multiple groups.
        #just providing a filter will kill the multi-sort-order
        qry = cls.query().\
            order(-MeetupEvent.status,MeetupEvent.time).iter()
        if qry.has_next():
            return qry
        else:
            return None

    @classmethod
    def getEvent(cls,event_id):
        """ Searches for an event that matches the arg(event_id).
        If nothing is found False is returned
        """
        events = cls.query(MeetupEvent.event_id == event_id).iter()
        event = False
        if events.has_next():
            event = events.next()
        return event

    def getEventComments(self):
        """ Returns the comments iterator for the current Event or
            False otherwise """
        comments = Comment.query(Comment.event_id == self.event_id).iter()
        return comments if comments.has_next() else False

    def filterComments(self,comments,status):
        """ Given an iterator over a Comment query, filters it. 

        Status:
        0   --  bad
        1   --  good

        Returns:
        List of comments if comments arg is not False
        False otherwise
        """
        return [comment for comment 
            in comments 
            if comment.bom == status] if comments else False



class MeetupMember(ndb.Model):
    member_id   = ndb.StringProperty(indexed=True,required=True)
    name        = ndb.StringProperty(indexed=True)
    group       = ndb.KeyProperty(kind=MeetupGroup,repeated=True)
    event       = ndb.KeyProperty(kind=MeetupEvent,repeated=True)


class MeetupLocation(ndb.Model):
    address_1   = ndb.StringProperty()
    address_2   = ndb.StringProperty()
    address_3   = ndb.StringProperty()
    venue_id    = ndb.StringProperty()
    lat_lon     = ndb.GeoPtProperty()
    name        = ndb.StringProperty()
    city        = ndb.StringProperty()
    event       = ndb.KeyProperty(kind=MeetupEvent)

