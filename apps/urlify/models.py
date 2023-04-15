from wsgic.database import database as db
from wsgic.database.columns import *

db.debug = False

class Urls(db.Model):
    short: str = Column(unique=True)
    target: str = UrlColumn()
    created: datetime = DateTimeColumn()
    last_used: datetime = DateTimeColumn()

    def __str__(self):
        return f"<Url: link='{self.short}' target='{self.target}'>"