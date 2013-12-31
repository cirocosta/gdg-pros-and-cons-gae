#inject conducts us to a problem: we need to match the 
#key of the object with the key of the other

def injectAttrs(injector,injected):
	""" Given to distinct objects inject the values from one object 
	to the other if the key matches"""
	injector = injector.__dict__
	for field in injected.__dict__:
		if injector.has_key(field):
			setattr(injected,field,injector[field])
		else:
			setattr(injected,field,None)
	return injected

#if the injected is a ndb.Model instance then we'll have problem with
#injectAttrs as the attributes of the model are in the 'values' field
#of the instance.


#DO NOT USE THIS HERE
def injectAttrsExpando(injector,injected):
	""" Populates the injected with the properties on injector.

	injector : instance with default __dict__
	injected : ndb.Expando instance
	"""
	injector = injector.__dict__
	for field in injector:
		try:
			setattr(injected,field,injector[field])
		except:
			setattr(injected,field,None)
	return injected