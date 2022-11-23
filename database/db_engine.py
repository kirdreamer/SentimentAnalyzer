from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from database.properties_module import DatabaseProperties

engine = create_engine(f'{DatabaseProperties.engine}://'
                       f'{DatabaseProperties.login}:'
                       f'{DatabaseProperties.password}@'
                       f'{DatabaseProperties.hostname}:'
                       f'{DatabaseProperties.port}/'
                       f'{DatabaseProperties.name}')
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()
