import sqlalchemy as s
import sqlalchemy.orm as so

database = s.create_engine('sqlite:///data.db', echo=True)
Connector = so.sessionmaker()
Myka = so.declarative_base()

class Senchiies(Myka):
    __tablename__ = "caNe4ku"
    id = s.Column(s.Integer(),primary_key = True)
    name = s.Column(s.String(250))
    x = s.Column(s.Integer())
    y = s.Column(s.Integer())

Myka.metadata.create_all(database)