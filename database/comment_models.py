from sqlalchemy import Column, Integer, String

from database.properties_module import DatabaseProperties
from database.db_engine import Base, engine


class Comment(Base):
    __tablename__ = DatabaseProperties.table

    id = Column(Integer, primary_key=True)
    body = Column(String)
    mood = Column(String)

    def __repr__(self):
        return f'Comment id: {self.id}, body: {self.body}'


Base.metadata.create_all(bind=engine)
