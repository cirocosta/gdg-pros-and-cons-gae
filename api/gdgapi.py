# Webapp API to serve whatever needs it

import endpoints

from protorpc import messages
from protorpc import message_types
from protorpc import remote
from votescreen.models import Comment


@endpoints.api(name='gdgapi',version='v1')
class GdgApi(remote.Service):
    """ GDGProsAndCons API , Version = 1 

    Paths:
        comment                 (PUT)     
        comment/{id}            (DELETE) 
        comment/{id}            (GET)
        comments/{event_id}     (GET)
    """

    @Comment.method(response_fields=('id',),
                    path='comment',
                    http_method='PUT',
                    name='comment.put')
    def CommentPut(self,comment):
        comment.put()
        return comment


    @Comment.method(request_fields=('id',),
                    response_fields=('id',),
                    path='comment/{id}',
                    http_method='DELETE',
                    name='comment.delete')
    def CommentDelete(self,comment):
        if not comment.from_datastore:
            raise endpoints.NotFoundException('Comment not found.')
        return comment


    @Comment.method(request_fields=('id',),
                    path='comment/{id}',
                    http_method='GET',
                    name='comment.get')
    def CommentGet(self,comment):
        if not comment.from_datastore:
            raise endpoints.NotFoundException('Comment not found.')
        return comment


    @Comment.query_method(query_fields=('limit', 'order', 'pageToken'),
                    path='comments/{event_id}',
                    name='comments.list')
    def CommentsList(self,query):
        return query

