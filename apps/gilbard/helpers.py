from wsgic.database.sqlite import SqliteDatabase
from wsgic.handlers.files import FileSystemStorage
from wsgic.helpers import get_global

database = SqliteDatabase("./db.sqlite", check_same_thread=False)

@database.on("error")
def error(e):
	raise e

appdir = FileSystemStorage(directory=get_global("appsdir"))[__package__]
media = appdir["media"].create()
