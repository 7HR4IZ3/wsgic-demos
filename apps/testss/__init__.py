from wsgic import WSGIApp
from wsgic.http import request

app = __app__ = WSGIApp()

@app.get("/")
def index():
    return f"Hello World from {request.path}"

print(app.routes)

application = app.wrapped_app("wsgi")
