from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Crear el motor de base de datos SQLite
engine = create_engine('sqlite:///../database.db')

# Crear la sesión
Session = sessionmaker(bind=engine)
session = Session()
