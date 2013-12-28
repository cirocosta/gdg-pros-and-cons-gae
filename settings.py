import os
import jinja2

DEBUG = True
JINJA_ENVIRONMENT = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.join(os.getcwd() + '/templates')),
    extensions = ['jinja2.ext.autoescape'],
    autoescape=True
    )

MEETUP_API_KEY = '464d442f5f463444366451a7d63726e'
MEETUP_GDG_GROUP_ID = '8562442'