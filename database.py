from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# IMPORTANT: Change YOUR_PASSWORD to the password you used for postgres
DATABASE_URL = "postgresql://postgres:password@localhost/bootcampdb"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()