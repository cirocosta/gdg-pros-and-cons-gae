# Hello World API implemented using Google Cloud Endpoints.

# Defined here are the ProtoRPC messages needed to define Schemas for methods
# as well as those methods defined in an API.

import endpoints

from protorpc import messages
from protorpc import message_types
from protorpc import remote
from api.api_messages import Greeting
from api.api_messages import GreetingCollection
from api.api_messages import STORED_GREETINGS


@endpoints.api(name='helloworld',version='v1')
class HelloWorldApi(remote.Service):
    """ Hellworld API V1. """

    @endpoints.method(message_types.VoidMessage, GreetingCollection,
                        path='hellogreeting', http_method='GET',
                        name='greetings.listGreeting')
    def greetings_list(self,unused_request):
        return STORED_GREETINGS

    MULTIPLY_METHOD_RESOURCE = endpoints.ResourceContainer(
            Greeting,
            times=messages.IntegerField(2,variant=messages.Variant.INT32,
                                        required=True))

    @endpoints.method(MULTIPLY_METHOD_RESOURCE,Greeting,
                        path='hellogreeting/{times}',
                        http_method='POST',
                        name='greetings.multiply')
    def greetings_multiply(self,request):
        return Greeting(message=request.message * request.times)


    ID_RESOURCE = endpoints.ResourceContainer(
            message_types.VoidMessage,
            id=messages.IntegerField(1, variant=messages.Variant.INT32))


    @endpoints.method(ID_RESOURCE, Greeting,
                        path='hellogreeting/{id}',
                        http_method='GET',
                        name='greetings.getGreeting')
    def greeting_get(self,request):
        try:
            return STORED_GREETINGS.items[request.id]
        except (IndexError,TypeError):
            return endpoints.NotFoundException('Greeting %s not found' %
                (request.id))
