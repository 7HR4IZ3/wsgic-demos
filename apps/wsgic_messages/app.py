from wsgic import WSGIApp
from wsgic.helpers import config

class MessagesApp(WSGIApp):
    def __init__(self):
        super().__init__("wsgic_messages.urls:router", config)

__app__ = MessagesApp()
