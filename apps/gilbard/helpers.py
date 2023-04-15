from wsgic.database.sqlite import SqliteDatabase
from wsgic.handlers.files import FileSystemStorage
from pathlib import Path

database = SqliteDatabase("./db.sqlite", check_same_thread=False)

@database.on("error")
def error(e):
	raise e

appdir = FileSystemStorage(directory=str(Path(__file__).parent.absolute()))
media = appdir["media"].create()
