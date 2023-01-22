from wsgic import WSGIApp
from wsgic.helpers import config

class ApitestApp(WSGIApp):
    def __init__(self):
        super().__init__("apitest.urls:router", config)

__app__ = ApitestApp()
