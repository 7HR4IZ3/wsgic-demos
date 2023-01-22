from wsgic.routing import Router
from wsgic_admin.app import __app__ as AdminApp

from .helpers import appdir, media
from .views import *

assets = appdir["assets"]

router, routes = Router().get_routes()

routes.static("/static", assets, name="static")
routes.static("/media", media)

routes.get("<locale>/translate/<name>", locale_test)
routes.add("*", index, methods="GET")

with routes.group("auth"):
    routes.add("/login", login, name="login")
    routes.get("logout", logout, name="logout")

routes.mount("/admin", AdminApp)
