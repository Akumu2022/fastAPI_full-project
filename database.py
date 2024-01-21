from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

URL_DATABASE = "mysql+pymysql://root:@localhost:3307/delivery"
engine =  create_engine(URL_DATABASE, echo=True)

Base = declarative_base()

Session = sessionmaker(autocommit=False,autoflush=False, bind=engine)
