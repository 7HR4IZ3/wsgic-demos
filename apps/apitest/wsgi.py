from .app import app as ApitestApp

application = ApitestApp.wrapped_app("wsgi")
