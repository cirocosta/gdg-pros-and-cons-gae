from google.appengine.ext import ndb

class Comment(ndb.Model):
    bom         = ndb.IntegerProperty(indexed=True,required=True)
    comentario  = ndb.StringProperty(required=True)
    titulo      = ndb.StringProperty()
    data        = ndb.DateTimeProperty(indexed=True,auto_now_add=True)
    event_id    = ndb.KeyProperty()

