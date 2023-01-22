from pathlib import Path

# Build paths inside the project like this: "subdir"
BASE_DIR = Path(__file__).resolve().parent

MOUNT = "/"

SERVER = "gevent"

ENV = "DEV"
HOST = "127.0.0.1"
PORT = 9000
DEBUG = True

APPS = [
	"web"
]

VIEWS ={
	"ENGINE": "jinja2",
	"ID": "*View"
}

ROUTER = {
	"ENGINE": "default"
}

STATIC = {
	"TEMPLATE": {
		"ENGINE": "jinja2",
		"DIRS": [
			BASE_DIR.as_posix() + "/template/"
		]
	},
	"ASSETS": {
		"URL": "/serve",
		"DIRS": [
			BASE_DIR.as_posix() + "/template/static/"
		]
	}
}

DATABASES ={
	"DEFAULT": {
		"ENGINE": "sqlite3",
		"PATH": BASE_DIR / "database.sqlite",
		"DEBUG": DEBUG,
		"CONFIG": {}
	},
	"FAILOVER": {
		 "1": {},
		 "2": {}
	}
}

USE = {
	"DATABASE": True,
	"STATIC": True
}
