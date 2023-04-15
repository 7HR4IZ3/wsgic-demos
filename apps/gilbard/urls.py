from wsgic.routing import Router
from wsgic_admin.app import __app__ as AdminApp

from .helpers import appdir, media
from .views import *

assets = appdir["assets"]

router, routes = Router().get_routes()

routes.view("/auth", AuthView, name="auth")
routes.view("/", HomeView, methods="GET")

routes.mount("/admin", AdminApp)

routes.static("/static", assets, name="static")
routes.static("/media", media)

print(routes.data)
