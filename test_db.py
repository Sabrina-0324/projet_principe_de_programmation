from database import SessionLocal

try:
    db = SessionLocal()
    print("Connexion réussie à la base PostgreSQL !")
finally:
    db.close()