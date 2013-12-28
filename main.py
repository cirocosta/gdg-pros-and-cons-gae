import webapp2
import settings
import index.views
import votescreen.views
import meetup_api.views

application = webapp2.WSGIApplication([
    ('/', index.views.IndexPage),
    ('/votescreen',votescreen.views.VoteScreen),
    ('/votescreen/einfo',votescreen.views.EInfo),
    ('/votescreen/vinfo',votescreen.views.VInfo),
    ('/meetup_api/refresh_db',meetup_api.views.RefreshDb),
], debug=settings.DEBUG)