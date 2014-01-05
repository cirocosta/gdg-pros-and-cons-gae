# Main handler for the requests. Routes the paths to the methods

import webapp2
import endpoints
import settings

import index.views
import votescreen.views
import meetup_api.views

from api.helloworld_api import HelloWorldApi


api_application = endpoints.api_server([
    HelloWorldApi,
]) 

application = webapp2.WSGIApplication([
    ('/',index.views.IndexPage),
    ('/votescreen/([a-zA-Z0-9]+)',
        votescreen.views.VoteScreen),
    ('/votescreen/([a-zA-Z0-9]+)/einfo',
        votescreen.views.EInfo),
    ('/votescreen/([a-zA-Z0-9]+)/vinfo',
        votescreen.views.VInfo),
    ('/meetup_api/refresh_db', 
        meetup_api.views.RefreshDb),
], debug=settings.DEBUG)