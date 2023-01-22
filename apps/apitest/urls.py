from wsgic.routing import Router
from .views import *

router = Router()
router.set_routes(routes)

# with routes.use(ProductsView()):
# 	routes.get("/", "index")
# routes.resource("/", ProductsView())