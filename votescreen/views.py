import webapp2
import settings

from meetup_api.models import MeetupEvent


class VoteScreen(webapp2.RequestHandler):
    def get(self,event_id):
        event = MeetupEvent().getEvent(event_id)
        comments = event.getEventComments()
        good_comments = event.filterComments(comments,1)
        bad_comments = event.filterComments(comments,1)
        
        template_values = {
            'event'  :   event,
            'good_comments':   good_comments,
            'bad_comments' :   bad_comments, 
            }

        template = settings.JINJA_ENVIRONMENT.get_template(
            'votescreen/votescreen.html')
        self.response.write(template.render(template_values))


class EInfo(webapp2.RequestHandler):
    def get(self,event_id):
        template_values = {
            'event' :   MeetupEvent().getEvent(event_id)  
        }
        template = settings.JINJA_ENVIRONMENT.get_template(
            'votescreen/einfo.html')
        self.response.write(template.render(template_values))


class VInfo(webapp2.RequestHandler):
    def get(self,event_id):
        template_values = {}
        template = settings.JINJA_ENVIRONMENT.get_template(
            'votescreen/vinfo.html')
        self.response.write(template.render(template_values))
