from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQLALCHEMY_DATABASE_URL="postgresql://postgres:kab123@localhost:5432/"
SQLALCHEMY_DATABASE_URL="postgresql://postgres:kab123@172.17.0.3:5432/"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()