# Webapp API to serve whatever needs it

import endpoints

from protorpc import messages
from protorpc import message_types
from protorpc import remote
from api import api_messages
from votescreen.models import Comment
from meetup_api.models import MeetupEvent



@endpoints.api(name='gdgapi',version='v1')
class GdgApi(remote.Service):
    """ GDGProsAndCons API , Version = 1 """

    COMMENT_RESOURCE = endpoints.ResourceContainer(
            api_messages.ApiComment,
            event_id=messages.IntegerField(
                2,
                variant=messages.Variant.INT32,
                required=True)
        )
    @endpoints.method(COMMENT_RESOURCE,ApiComment,
                        path='comment/{event_id}',
                        http_method="POST",
                        name='comment.post')
    def commentPost(self,request):
        """ Posts a comment and returns the ID of the comment in 
            the database after the insertion"""
        comment = api_messages.Comment(
                        parent=ndb.Key('Comment',request.evento),
                        bom=request.bom,
                        comentario=request.comentario,
                        data=request.data,
                        event_id=request.event_id,
                        titulo=request.titulo)
        comment.put()
        return api_messages.ApiDefaultResponse(
                        position=comment.key.id())

    ID_RESOURCE = endpoints.ResourceContainer(
            message_types.VoidMessage,
            id=messages.IntegerField(
                1,
                variant=messages.Variant.INT32,
                required=True)
        )

    #id == event_id
    # @endpoints.method(ID_RESOURCE, ApiCommentCollection,
    #                     path='comments/{id}',
    #                     http_method='GET',
    #                     name='comments.get')
    # def commentsGet(self,request):
    #     event = MeetupEvent().getEvent(event_id=request.id)
    #     comments = event.getEventComments()

