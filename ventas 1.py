import sqlite3
from datetime import datetime

class EnvioManager:

    def __init__(self, db_name):

        self.db_name = db_name

def create(self, id_cliente, id_paquete, id_destino, estado_envio):

    fecha_envio = datetime.now().strftime("%Y-%m-%d")

    with sqlite3.connect(self.db_name) as conn:

        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO envios
        (id_cliente, id_paquete, id_destino, fecha_envio, estado_envio)
        VALUES (?, ?, ?, ?, ?)
        """, (id_cliente, id_paquete, id_destino, fecha_envio, estado_envio))

        conn.commit()

def read(self):

    with sqlite3.connect(self.db_name) as conn:

        cursor = conn.cursor()

        cursor.execute("SELECT * FROM envios")

        return cursor.fetchall()

class EnvioInteractivo:

    def __init__(self, db_name):

        self.manager = EnvioManager(db_name)