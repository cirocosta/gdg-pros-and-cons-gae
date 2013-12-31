from meetup_api.models import MeetupEvent
from meetup_api.models import MeetupGroup
from google.appengine.ext import ndb

import webapp2
import settings


class IndexPage(webapp2.RequestHandler):
    def get(self):
        try:
            group = MeetupGroup().query(ndb.GenericProperty('urlname') == 'GDG-SP')\
                .iter().next()
            events = MeetupEvent().getGroupEvents(group.key)
        except StopIteration:
            group = None
            events = None

        print events
        main_event = events.next() if events != None else False
        template_values = {
            'main_event'    :   main_event,
            'events'        :   events if events != None else False,
        }
        
        template = settings.JINJA_ENVIRONMENT.get_template('index/index.html')
        self.response.write(template.render(template_values))
