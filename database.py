from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#pip install psycopg2-binary ---python connector postgresql to mysql

engine = create_engine("postgresql://postgres:password@localhost/dbname")
    echo=True 
    
Base = declarative_base()
