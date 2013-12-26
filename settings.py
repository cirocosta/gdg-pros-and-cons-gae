import os
import jinja2

DEBUG = True
JINJA_ENVIRONMENT = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.join(os.getcwd() + '/templates')),
    extensions = ['jinja2.ext.autoescape'],
    autoescape=True
    )
