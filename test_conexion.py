import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()
engine = create_engine(os.getenv("DB_URL"))

with engine.connect() as conexion:
    resultado = conexion.execute(text("SELECT version()"))
    print(resultado.scalar())
