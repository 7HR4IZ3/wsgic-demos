import functools

from wsgic.http import redirect, request, BaseResponse
from wsgic.services import service
from wsgic_auth.authorization import Authorization
from wsgic_auth.core import SessionAuth

authentication: SessionAuth = service("authentication")
authorization: Authorization = service("authorization")

# auth = Cork(backend=SQLiteBackend(db, User, Role, PendingReg, initialize=True), email_sender='federico.ceratto@gmail.com', smtp_url='smtp://smtp.magnet.ie')


def check(validate, fail=None, error="", back=None):
    def wrapper(func):
        @functools.wraps(func)
        def wrapped(*a, **kw):
            if validate(request):
                return func(*a, **kw)
            else:
                if callable(fail):
                    return fail()
                elif isinstance(fail, str):
                    return redirect().route(fail).error(error).with_next(request.path if back else None)
                elif isinstance(fail, BaseResponse):
                    return fail.with_next(request.path if back else None)
                else:
                    redirect('/').error(error).with_next(request.path if back else None)
        return wrapped
    return wrapper

def login_required(fail=None, error="Authentication Required", back=None):

    def wrapper(func):
        @functools.wraps(func)
        def wrapped(*a, **kw):
            print(request.user)
            if request.user:
                return func(*a, **kw)
            else:
                if callable(fail):
                    return fail()
                elif isinstance(fail, str):
                    return redirect().route(fail).error(error).with_next(request.path if back else None)
                elif isinstance(fail, BaseResponse):
                    return fail.with_next(request.path if back else None)
                else:
                    return redirect('/').error(error).with_next(request.path if back else None)
        return wrapped

    return wrapper

def restricted(role, fail=None, error="Access prohibited", back=None):

    def decorator(func):

        @functools.wraps(func)
        def wrapper(*a, **kw):
            if request.user:
                if request.user.role.role == role:
                    return func(*a, **kw)

            if callable(fail):
                return fail()
            elif isinstance(fail, str):
                return redirect().route(fail).error(error).with_next(request.path if back else None)
            elif isinstance(fail, BaseResponse):
                return fail.with_next(request.path if back else None)
            else:
                return redirect('/').error(error).with_next(request.path if back else None)

        return wrapper

    return decorator