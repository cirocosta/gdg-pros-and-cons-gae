import webapp2
import index.views
import settings

application = webapp2.WSGIApplication([
    ('/', index.views.IndexPage),
], debug=settings.DEBUG)