from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API bibliothèque fonctionne !"}


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Remplace USER, PASSWORD et DBNAME par tes informations
DATABASE_URL = "postgresql+psycopg2://USER:PASSWORD@localhost:5432/library_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()