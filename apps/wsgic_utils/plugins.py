from wsgic.plugins import *
from wsgic.helpers import load

class InstalledAppsPlugin:
	name ="installed_apps"
	api = 2

	def setup(self, app):
		installed_apps = app.config.get("installed_apps", [])
		for app in installed_apps:
			if isinstance(app, str):
				app = load(app)
			if hasattr(app, "__app__"):
				app = app.__app__
			app.setup()
