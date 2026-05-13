import sqlite3
import pandas as pd

class ClienteManager:

    def __init__(self, db_name):
        self.db_name = db_name

def create(self, id_cliente, email, telefono, fecha_nacimiento, nombre_cliente, tipo_cliente):

    with sqlite3.connect(self.db_name) as conn:

        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO clientes
        VALUES (?, ?, ?, ?, ?, ?)
        """, (id_cliente, email, telefono, fecha_nacimiento, nombre_cliente, tipo_cliente))

        conn.commit()

def read(self):

    with sqlite3.connect(self.db_name) as conn:

        cursor = conn.cursor()

        cursor.execute("SELECT * FROM clientes")

        return cursor.fetchall()

def delete(self, id_cliente):

    with sqlite3.connect(self.db_name) as conn:

        cursor = conn.cursor()

        cursor.execute("DELETE FROM clientes WHERE id_cliente = ?", (id_cliente,))

        conn.commit()

class ClienteDataCleaner:

    def __init__(self, db_name):
        self.db_name = db_name

def limpiar_datos(self):

    with sqlite3.connect(self.db_name) as conn:

        df = pd.read_sql_query("SELECT * FROM clientes", conn)

        df["nombre_cliente"] = df["nombre_cliente"].astype(str).str.title().str.strip()

        df["tipo_cliente"] = df["tipo_cliente"].astype(str).str.title().str.strip()

        df["email"] = df["email"].astype(str).str.lower().str.strip()

        df.to_sql("clientes", conn, if_exists="replace", index=False)
        class ClienteInteractivo:

            def __init__(self, db_name):

                self.manager = ClienteManager(db_name)

                self.cleaner = ClienteDataCleaner(db_name)