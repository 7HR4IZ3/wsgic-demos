# from argparse import ArgumentParser
# from wsgic.scripts import ParserScripts
# import requests
# import json

# class db(ParserScripts):
#     parser = ArgumentParser()
#     opt = parser.add_argument
#     # opt("-m", "--migrate", action="store_true", help="show version number.")
#     # opt("-b", "--bind", metavar="ADDRESS", help="bind socket to ADDRESS.")
#     # opt("-se", "--server", help="use SERVER as backend.")
#     # opt("-p", "--plugin", action="append", help="install additional plugin/s.")
#     # #  opt("-c", "--conf", action="append", metavar="FILE", help="load config values from FILE.")
#     # opt("-C", "--param", action="append", metavar="NAME=VALUE", help="override config values.")
#     # opt("-n", "--new", action="store_true", help="create new wsgi app.")
#     # opt("-s", "--script", action="store_true", help="run script then app.")
#     # opt("-a", "--asgi", action="store_true", help="run the asgi version of an app.")
#     # opt("-d", "--django", action="store_true", help="Run the django cli.")
#     # opt("-env", default="dev", help="set app environment")
#     # opt("--debug", action="store_true", help="start server in debug mode.")
#     # opt("--reload", action="store_true", help="auto-reload on file changes.")
#     opt('action', help='WSGI app entry point.', nargs='*')

#     parser = parser.parse_args
    
#     def __post_init__(self):
#         if self.args.action[0] == "migrate":
#             self.migrate()

#     def migrate(self):
#         print("Migrated")

# class cli:
#     def __init__(self, path="/", data=None):
#         ret = requests.request("cli", f"http://127.0.0.1:8100{path}", json=json.loads(data or {}))
#         print(ret.text)
from wsgic_auth.scripts import *

