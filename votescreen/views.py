import webapp2
import settings

class VoteScreen(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        template = settings.JINJA_ENVIRONMENT.get_template('votescreen/votescreen.html')
        self.response.write(template.render(template_values))

class EInfo(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        template = settings.JINJA_ENVIRONMENT.get_template('votescreen/einfo.html')
        self.response.write(template.render(template_values))


class VInfo(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        template = settings.JINJA_ENVIRONMENT.get_template('votescreen/vinfo.html')
        self.response.write(template.render(template_values))

