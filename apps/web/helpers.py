from wsgic.database.sqlite import SqliteDatabase

database = SqliteDatabase("./db.sqlite", check_same_thread=False)

@database.on("error")
def error(e):
	raise e
