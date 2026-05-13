import sqlite3
import pandas as pd

class PaqueteManager:

        def __init__(self, db_name):

            self.db_name = db_name

def create(self, id_paquete, peso, destino, estado):

    if peso < 1:
        tipo_paquete = "Documento"

    elif peso < 10:
        tipo_paquete = "Paqueteria"

    else:
        tipo_paquete = "Carga"

    costo_envio = peso * 5000

    with sqlite3.connect(self.db_name) as conn:

        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO paquetes
        VALUES (?, ?, ?, ?, ?, ?)
        """, (id_paquete, peso, destino, tipo_paquete, costo_envio, estado))

        conn.commit()

def read(self):

    with sqlite3.connect(self.db_name) as conn:

        cursor = conn.cursor()

        cursor.execute("SELECT * FROM paquetes")

        return cursor.fetchall()

class PaqueteDataCleaner:

    def __init__(self, db_name):

        self.db_name = db_name

    def limpiar_datos(self):

        with sqlite3.connect(self.db_name) as conn:

            df = pd.read_sql_query("SELECT * FROM paquetes", conn)

            df["destino"] = df["destino"].astype(str).str.title().str.strip()

            df["estado"] = df["estado"].astype(str).str.title().str.strip()

            df.to_sql("paquetes", conn, if_exists="replace", index=False)

class PaqueteInteractivo:

        def __init__(self, db_name):

            self.manager = PaqueteManager(db_name)

            self.cleaner = PaqueteDataCleaner(db_name)