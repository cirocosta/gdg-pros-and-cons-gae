# Webapp API to serve whatever needs it

import endpoints

from protorpc import messages
from protorpc import message_types
from protorpc import remote
from votescreen.models import Comment
from meetup_api.models import MeetupGroup, MeetupEvent


@endpoints.api(name='gdgapi',version='v1')
class GdgApi(remote.Service):
    """ GDGProsAndCons API , Version = 1 

    Paths:
        comment                 (PUT)     
        comment/{id}            (DELETE) 
        comment/{id}            (GET)
        comments/{event_id}     (GET)

        meetupevent
        meetupevents
        meetupgroup
        meetupgroups
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
                    path='comment',
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


    @MeetupGroup.method(request_fields=('group_id',),
                    path='meetupgroup',
                    http_method='GET',
                    name='meetupgroup.get')
    def MeetupGroupGet(self,group):
        if not group.from_datastore:
            raise endpoints.NotFoundException('MeetupGroup not found.')
        return group

    @MeetupGroup.query_method(query_fields=('limit','order','pageToken',),
                        path='meetupgroups',
                        name='meetupgroups.list')
    def MeetupGroupsList(self,query):
        return query


    @MeetupEvent.query_method(query_fields=('limit','order','pageToken',),
                        path='meetupgevents',
                        name='meetupevents.list')
    def MeetupEventsList(self,query):
        return query

    @MeetupEvent.method(request_fields=('event_id',),
                        path='meetupevent',
                        http_method='GET',
                        name='meetupevent.get')
    def MeetupEventGet(self,event):
        if not event.from_datastore:
            raise endpoints.NotFoundException('MeetupEvent not found.')
        return event