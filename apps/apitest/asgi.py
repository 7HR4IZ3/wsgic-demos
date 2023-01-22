from .app import __app__ as ApitestApp

application = ApitestApp.wrapped_app("asgi")
