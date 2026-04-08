from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Configuration de la connexion à PostgreSQL
SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost:5432/nom_de_la_base"

#Créer un moteur de base de données
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

#Session locale pour interagir avec la DB
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Base pour les modèles
Base = declarative_base()