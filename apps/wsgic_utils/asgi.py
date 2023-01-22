from .app import __app__ as Wsgic_UtilsApp

application = Wsgic_UtilsApp.wrapped_app("asgi")
