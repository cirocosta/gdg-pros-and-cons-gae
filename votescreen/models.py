from google.appengine.ext import ndb
from endpoints_proto_datastore.ndb import EndpointsModel


class Comment(EndpointsModel):
    _message_fields_schema = (
        'id','bom','comentario','titulo','data','event_id',
        )

    bom         = ndb.IntegerProperty(indexed=True,required=True)
    comentario  = ndb.StringProperty(required=True)
    titulo      = ndb.StringProperty()
    data        = ndb.DateTimeProperty(indexed=True,auto_now_add=True)
    event_id    = ndb.KeyProperty()

