from pathlib import Path
from werkzeug.middleware.lint import LintMiddleware
# from jinja2.


BASE_DIR = Path(__file__).resolve().parent

ENV = "DEV"
DEBUG = False

SERVER = {
    "host": "127.0.0.1",
    "port": 8100,
    "debug": DEBUG
}

LOGIN_REDIRECT = '/'
LOGOUT_REDIRECT = 'admin_login'

HOOKS = {
    "app_start": [],
    "before_request": [],
    "after_request": [],
    "app_stop": []
}

MIDDLEWARES = {
    "WSGI": [
        LintMiddleware
    ]
}

INSTALLED_APPS = [
    "wsgic_admin"
]

PLUGINS = [
    # "wsgic.session.plugins:SessionPlugin",
    # "wsgic.http.plugins:RequestPlugin",
    # "wsgic.http.plugins:ResponsePlugin",
    "wsgic.ext.auth.plugins:AuthPlugin",
    # "wsgic.ext.auth.plugins:JWTPlugin",
    "wsgic.services.validation.plugins:ValidationPlugin",
    # "wsgic.utils.i18n.plugins:I18nPlugin" # Fix this!!
]

STATIC = {
    "TEMPLATE": {
        "ENGINE": "wsgic.views.templates:Jinja2Template",
        "DIRS": [
            BASE_DIR / "templates/",
            BASE_DIR / "{app_name}/template/",
            BASE_DIR / "{app_name}/templates/",
        ],
        "CONFIG": {
            # "block_start_string": BLOCK_START_STRING,
            # "block_end_string": BLOCK_END_STRING,
            # "variable_start_string": VARIABLE_START_STRING,
            # "variable_end_string": VARIABLE_END_STRING,
            # "comment_start_string": COMMENT_START_STRING,
            # "comment_end_string": COMMENT_END_STRING,
            # "line_statement_prefix": LINE_STATEMENT_PREFIX,
            # "line_comment_prefix": LINE_COMMENT_PREFIX,
            # "trim_blocks": TRIM_BLOCKS,
            # "lstrip_blocks": LSTRIP_BLOCKS,
            # "newline_sequence": NEWLINE_SEQUENCE,
            # "keep_trailing_newline": KEEP_TRAILING_NEWLINE,
            # "extensions":(), 
            # "optimized": True,
            # "undefined": Undefined,
            # "finalize": None,
            # "autoescape": False,
            # "loader": None,
            # "cache_size": 400,
            # "auto_reload": True,
            # "bytecode_cache": None,
            # "enable_async": False
        }
    },
    "ASSETS": {
        "STORE": "wsgic.handlers.files:FileSystemStorage",
        "URL": "/assets",
        "DIR": "./templates/assets/"
    }
}

DATABASES = {
    "SQLITE": {
        "PATH": "./database.sqlite",
        "DEBUG": False,
        'VERBOSE': False,
        "CONFIG": {
            "check_same_thread": False
        }
    },
    "JSON": {
        "PATH": "./database.json",
        "DEBUG": DEBUG
    },
    "FAILOVERS": {
        "1": {},
        "2": {}
    }
}

DATABASE = {
    "PATH": "sqlite://database.sqlite",
    "DEBUG": DEBUG,
    "VERBOSE": DEBUG,
    "CONFIG": {
        "check_same_thread": False
    }
}

ADMIN = {
    "TEMPLATES": {
        "ACTIVITIES": "admin/activities3.html"
    }
}

USE = {
    "DATABASE": True,
    "STATIC": True,
    "SESSION": True,
    "ENDSLASH": False
}

CLASSES = {
    'DATABASE': 'wsgic.database.sqlite:SqliteDatabase',
    'SESSION': 'wsgic.session:Session',
    'REQUEST': 'wsgic.server:Request',
    'RESPONSE': 'wsgic.server:Response'
}

SESSION = {
    'CLASS': 'wsgic.session:Session',
    'STORE': 'wsgic.session.stores:DatabaseSessionStore',
    'DICT': 'wsgic.session:SessionDict',

    "COOKIE": {
        "name": "wsgic_session",
        "path": "/",
        "expires": None, # None
        "maxage": 3600 * 24 * 31,
        "secret": "wsgic_default_secret_key-jufjjgvssbionit4e4we6jbd4ri9k8",
        "secure": False,
        "domain": None,
        "httponly": False,
        "samesite": "Lax"
    } 
}

LOCALE = {
    "DEFAULT": "en",
    "SUPPORTED": ["en", "de"]
}
