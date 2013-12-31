from google.appengine.ext import ndb

EVENT_STATUS = {
    "canceled"  :   0,
    "upcoming"  :   1,
    "past"      :   2,
    "proposed"  :   3,
    "suggested" :   4,
    "draft"     :   5,
}


class MeetupGroup(ndb.Expando):
    """ Utilizing ndb.Expando to show how easy it is to use this with
    the model of API that we've built. """
    group_id    = ndb.StringProperty(indexed=True,required=True)


class MeetupEvent(ndb.Model):
    event_id            = ndb.StringProperty(indexed=True,required=True)
    name                = ndb.StringProperty(indexed=True)
    time                = ndb.DateTimeProperty(indexed=True)
    description         = ndb.TextProperty()
    duration            = ndb.IntegerProperty()
    event_url           = ndb.StringProperty()
    maybe_rsvp_count    = ndb.IntegerProperty()
    yes_rsvp_count      = ndb.IntegerProperty()
    photo_url           = ndb.StringProperty()
    status              = ndb.StringProperty()
    updated             = ndb.DateTimeProperty(indexed=True)
    group               = ndb.KeyProperty(kind=MeetupGroup)


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

