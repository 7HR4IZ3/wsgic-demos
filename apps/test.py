import types
from bottle import load
from django.urls.resolvers import URLResolver, URLPattern
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djng.settings')

routes = []

class Route:
	def __init__(self, rule, method, callback, name=None, plugins=None, skiplist=None, **config):
		#: The path-rule string (e.g. ``/wiki/<page>``).
		self.rule = rule
		#: The HTTP method as a string (e.g. ``GET``).
		self.method = method
		#: The original callback with no plugins applied. Useful for introspection.
		self.callback = callback
		#: The name of the route (if specified) or ``None``.
		self.name = name or None
		#: A list of route-specific plugins (see :meth:`Bottle.route`).
		self.plugins = plugins or []
		#: A list of plugins to not apply to this route (see :meth:`Bottle.route`).
		self.skiplist = skiplist or []
		#: Additional keyword arguments passed to the :meth:`Bottle.route`
		#: decorator are stored in this dictionary. Used for route-specific
		#: plugin configuration and meta-data.
		self.config = config
	
	def re_init(self, app):
		self.app = app
		self.config = app.config._make_overlay().load_dict(self.config)
		return self
	
	def __repr__(self):
		cb = self.callback
		return '<%s %s -> %s:%s>' % (self.method, self.rule, cb.__module__, cb.__name__)

def remake_url(url):
	if "/" in url:
		new = "/".join([remake_url(u) for u in url.split("/")])

	if ":" in url and "<" in url and ">" in url:
		lb = url.find("<")
		rb = url.find(">")
		new = url[lb+1:rb]
		
		left, right = new.split(":")
		new = "<" + ":".join([right, left]) + ">"
	else:new = url
	return new

def process_pattern(pattern, path=""):
	name = pattern.name
	path = path + str(pattern.pattern)
	callback = pattern.callback
	routes.append(Route(remake_url(str(path)), ["GET", "POSTS", "PUT", "DELETE"], callback, name=name))

def process_resolver(resolver, path=""):
	name = resolver.urlconf_name
	path = path + str(resolver.pattern)
	callback = resolver.callback

	# print("resolver:", remake_url(str(path)), callback)
	if isinstance(name, list):
		for item in name:
			if isinstance(item, URLPattern):
				process_pattern(item, path)
			elif isinstance(item, URLResolver):
				process_resolver(item, path)
	elif isinstance(name, types.ModuleType):
		for item in name.urlpatterns:
			if isinstance(item, URLPattern):
				process_pattern(item, path)
			elif isinstance(item, URLResolver):
				process_resolver(item, path)

def make_django_routes(urls):
	allurls = urls.urlpatterns
	for url in allurls:
		if isinstance(url, URLResolver):
			process_resolver(url)
		elif isinstance(url, URLPattern):
			process_pattern(url)

load("djng.wsgi")
make_django_routes(load("djng.urls"))

for x in routes:
	print(repr(x))