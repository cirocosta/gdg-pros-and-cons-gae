import webapp2
import settings
import index.views
import votescreen.views


application = webapp2.WSGIApplication([
    ('/', index.views.IndexPage),
    ('/votescreen',votescreen.views.VoteScreen),
    ('/votescreen/einfo',votescreen.views.EInfo),
    ('/votescreen/vinfo',votescreen.views.VInfo),
], debug=settings.DEBUG)