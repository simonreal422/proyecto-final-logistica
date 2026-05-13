import sqlite3
import pandas as pd

class DestinoManager:

    def __init__(self, db_name):

        self.db_name = db_name

def create(self, id_destino, ciudad, departamento, zona):

    with sqlite3.connect(self.db_name) as conn:

        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO destinos
        VALUES (?, ?, ?, ?)
        """, (id_destino, ciudad, departamento, zona))

        conn.commit()

def read(self):

    with sqlite3.connect(self.db_name) as conn:

        cursor = conn.cursor()

        cursor.execute("SELECT * FROM destinos")

        return cursor.fetchall()

class DestinoDataCleaner:

    def __init__(self, db_name):

        self.db_name = db_name

def limpiar_datos(self):

    with sqlite3.connect(self.db_name) as conn:

        df = pd.read_sql_query("SELECT * FROM destinos", conn)

        df["ciudad"] = df["ciudad"].astype(str).str.title().str.strip()

        df["departamento"] = df["departamento"].astype(str).str.title().str.strip()

        df["zona"] = df["zona"].astype(str).str.title().str.strip()

        df.to_sql("destinos", conn, if_exists="replace", index=False)

class DestinoInteractivo:

    def __init__(self, db_name):

        self.manager = DestinoManager(db_name)

        self.cleaner = DestinoDataCleaner(db_name)