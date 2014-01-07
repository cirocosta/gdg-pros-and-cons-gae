# Contains all of the code that is particular to the messages that are
# delivered. These objects are a mapping to what will be show in the
# response that the API will give and also the body of requests.

from protorpc import messages
from protorpc import message_types
from protorpc import remote


class Greeting(messages.Message):
    """ Greeting that stores a message. """
    message = messages.StringField(1)


class GreetingCollection(messages.Message):
    """ Collection of Greetings """
    items = messages.MessageField(Greeting,1,repeated=True)


STORED_GREETINGS = GreetingCollection(items=[
    Greeting(message='Hello World!'),
    Greeting(message='goodbye F*Cking World'),
])
<<<<<<< HEAD
=======


class ApiDefaultResponse(messages.Message):
	position 	=	messages.IntegerField(1)


class ApiComment(messages.Message):
	bom			=	messages.IntegerField(1)
	comentario	=	messages.StringField(2)
	titulo		=	messages.StringField(3)
	data		=	messages.IntegerField(4)
	event_id	=	messages.StringField(5)

class ApiCommentCollection(messages.Message):
	comments 	= 	messages.MessageField(ApiComment,
								1,repeated=True)
>>>>>>> F_api
