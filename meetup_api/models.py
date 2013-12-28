from google.appengine.ext import ndb

class MeetupGroup(ndb.Model):
	name = ndb.StringProperty()
	description = ndb.TextProperty()
	primary_topic = ndb.StringProperty()
	organizer = ndb.StringProperty()

class MeetupMember(ndb.Model):
	name = ndb.StringProperty()

class MeetupEvent(ndb.Model):
	name = ndb.StringProperty()
