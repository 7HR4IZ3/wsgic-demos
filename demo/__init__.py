from wsgic import WSGIApp

app = WSGIApp()

@app.get("/")
def index():
    return f"Hello World"

application = app.wrapped_app("wsgi")
