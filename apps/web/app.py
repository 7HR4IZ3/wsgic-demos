from wsgic import WSGIApp
from wsgic.helpers import config


class WebApp(WSGIApp):
	pass


__app__ = WebApp("web.urls:router", config)
__app__.catchall = False
