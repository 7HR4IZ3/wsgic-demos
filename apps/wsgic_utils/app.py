from wsgic import WSGIApp
from wsgic.helpers import config

class Wsgic_UtilsApp(WSGIApp):
    def __init__(self):
        super().__init__("wsgic_utils.urls:router", config)

__app__ = Wsgic_UtilsApp()
