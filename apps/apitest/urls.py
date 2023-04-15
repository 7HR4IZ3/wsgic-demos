from wsgic.routing import Router
from wsgic_api.views import SwaggerView
from .views import *

router = Router(routes)

@routes.view("/swagger")
class SwaggerUI(SwaggerView):
    router = router

# with routes.use(ProductsView()):
# 	routes.get("/", "index")
# routes.resource("/", ProductsView())