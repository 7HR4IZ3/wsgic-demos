from wsgic.database import columns, database

DEBUG = True
database.debug = DEBUG

@database.on("error")
def error(err):
    raise err

# database = sqlite.SqliteDatabase("./apitest.sqlite3", DEBUG, DEBUG, check_same_thread=False)

