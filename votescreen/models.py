from google.appengine.ext import ndb
from meetup_api.models import MeetupEvent

class Comment(ndb.Model):
	bom			= ndb.BooleanProperty(indexed=True,required=True)
	comentario 	= ndb.StringProperty()
	titulo 		= ndb.StringProperty()
	data		= ndb.DateTimeProperty(indexed=True,auto_now_add=True)
	evento 		= ndb.KeyProperty(kind=MeetupEvent)