# -*- coding: utf-8 -*-

#Super Simple Meetup API custom purpose lib.
#https://github.com/cirocosta/gdg-pros-and-cons-gae
#
#This is not the best for GAE as it does not
#translates directly for ndb.Model, but better
#for a general purpose


import json as simplejson
import urllib
import urllib2
import settings
import datetime

API_ROOT_2      = '2/'
API_ROOT_EW     = 'ew/'
API_HOST        = 'api.meetup.com/'
API_SCHEME      = 'https://'
    
URI_RSVPS       = 'rsvps/'
URI_PROFILES    = 'profiles/'
URI_GROUPS      = 'groups/'
URI_EVENTS      = 'events/'
URI_MEMBERS     = 'members/'


def convertToUtf8Str(param):
    """ To avoid the problem with non-ascii characters """
    if isinstance(param, unicode):
        param = param.encode('utf-8')
    elif not isinstance(param, str):
        param = str(param)
    return param

class MeetupApiException(Exception):
    pass


class MeetupApi(object):
    """ Class for the MeetupApi

    params for config:
    api_key     : api key on meetup
    api_root    : root for the api ('\ew' or '\2')
    api_scheme  : https or http
    host        : url host for the api
    """

    REQUIRED_FIELDS = {
        'events'    :   ['event_id','group_domain','group_id','group_urlname','member_id','rsvp','value_id'],
        'groups'    :   ['category_id','country,city,state','domain','group_id','group_urlname','lat,lon',\
            'member_id,','organizer_id','topic','topic,groupnum','zip'],
        'rsvps'     :   ['event_id','member_id'],
        'profiles'  :   ['group_id','group_urlname','member_id','topic,groupnum'],
        'members'   :   ['group_id','group_urlname','member_id','service','topic,groupnum'],
    }
    
    def __init__(self,api_key=settings.MEETUP_API_KEY):
        self.retry_count = 0
        self.retry_delay = 0
        self.api_key = api_key
        self.api_scheme = API_SCHEME
        self.api_host = API_HOST
        self.path = self.api_scheme + self.api_host

    def buildPath(self,model,api_root=API_ROOT_2,**params):
        """ Uses the object parameters to construct the path for the api fetching"""
        parameters_path = '%s?key=%s&' % (model,self.api_key)
        parameters_path += urllib.urlencode(params['params'])
        return self.path + api_root + parameters_path

    def getAllObjects(self,model,num=20,**params):
        """ Returns a list of objects of a model given some request params 

        params:
        model   -- the type of thing is being queried against
        num     -- limit of the result
        params  -- the params to obtain it
        """
        self.validateParameters(model,params)
        url = self.buildPath(model=model,api_root=API_ROOT_2,params=params)
        result = list()
        groups = list()
        try:
            response = simplejson.loads(urllib2.urlopen(url).read())
        except Exception,e:
            raise MeetupApiException('An exception was raised while getting the response: '\
                + str(e))
        if 'results' in response:
            results = response['results']
            if model == 'groups':
                for result in results:
                    groups.append(Group(result))
            elif model == 'events':
                for result in results:
                    groups.append(Event(result))
            elif model == 'members':
                for result in results:
                    groups.append(Member(result))
        if len(groups) > 0:
            return groups[0:num]
        else:
            return groups

    def validateParameters(self,model,parameters):
        """ Verifies if there is at least one of the required parameters for the query """
        required_params = self.REQUIRED_FIELDS[model]
        i = 0
        for param in parameters:
            if param in required_params:
                i += 1
        if i == 0:
            raise MeetupApiException("There's a lack of required params.")

    def __str__(self):
        return "Getting on %s with APIKey=%s" %(self.path,self.api_key)


class Model(object):
    """ Abstract class for the objects that we want to get.

    params:
    properties  --- Dict of the things we receive
    """
    fields = []

    def __init__(self,properties):
        for field in self.fields:
            try:
                value = properties[field]
                if type(value) != dict:
                    self.__setattr__(field,convertToUtf8Str(properties[field]))
                else:
                    self.__setattr__(field,properties[field])                    
            except:
                self.__setattr__(field,None)


class Event(Model):
    fields = ['announced','comment_count','created','description','distance',
        'duration','email_remainders','event_hosts','event_url','featured',
        'fee','group','headcount','how_to_find_us','id','is_simplehtml',
        'maybe_rsvp_count','name','photo_album_id','photo_count','photo_url',
        'publish_status','rating','rsvp_alerts','rsvp_rules','rsvpable','self',
        'short_link','status','survey_questions','time','timezone','trending_rank',
        'updated','utc_offset','venue','venue_visibility','visibility','why',
        'yes_rsvp_count'
        ]


class Member(Model):
    fields = ['bio','birthday','country,city,state','email','gender','hometown',
        'id','joined','lang','lat,lon','link','membership_count','messagable',
        'messaging_pref','name','other_services','photo','photo_url','photos',
        'privacy','reachable','self','topics','visited'
        ]


class Profile(Model):
    fields = ['additional','answers','attendance_count','bio','comment',
        'created,updated','group','member_city','member_country','member_id',
        'member_state','membership_dues','name','other_services','photo',
        'photo_url','profile_url','role','site_url,site_name','status',
        'title','visited'
        ]


class Group(Model):
    fields = ['category','city','country','created','description','ga_code',
        'group_photo','id','is_simplehtml','join_info','join_mode','lat','link',
        'list_addr','list_mode','lon','members','membership_dues','name',
        'next_event','organizer','other_services','pending_members','photos',
        'primary_topic','rating','self','short_link','similar_groups','sponsors',
        'state','timezone','topics','urlname','visibility','welcome_message','who'
        ]


class Rsvp(Model):
    fields = []
