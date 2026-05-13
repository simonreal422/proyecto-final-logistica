import sqlite3
import pandas as pd
import io
import tkinter as tk

# =========================================================
# IMPORTACIONES DE DATOS
# =========================================================
from datos import (
    csv_clientes,
    csv_paquetes,
    csv_destinos,
    csv_envios
)

# =========================================================
# IMPORTACIÓN DEL FRONTEND
# =========================================================
from app_central import AppCentral

# =========================================================
# NOMBRE BASE DE DATOS
# =========================================================
DB_NAME = "meta_logistica.db"

# =========================================================
# FUNCIÓN PARA CARGAR LA BASE DE DATOS
# =========================================================
def cargar_db():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()

        # =========================================================
        # TABLA CLIENTES
        # =========================================================
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id_cliente INTEGER PRIMARY KEY,
            email TEXT NOT NULL,
            telefono TEXT NOT NULL,
            fecha_nacimiento TEXT NOT NULL,
            nombre_cliente TEXT NOT NULL,
            tipo_cliente TEXT NOT NULL
        )
        """)

        # =========================================================
        # TABLA PAQUETES
        # =========================================================
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS paquetes (
            id_paquete INTEGER PRIMARY KEY,
            peso REAL NOT NULL,
            destino TEXT NOT NULL,
            tipo_paquete TEXT NOT NULL,
            costo_envio REAL NOT NULL,
            estado TEXT NOT NULL
        )
        """)

        # =========================================================
        # TABLA DESTINOS
        # =========================================================
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS destinos (
            id_destino INTEGER PRIMARY KEY,
            ciudad TEXT NOT NULL,
            departamento TEXT NOT NULL,
            zona TEXT NOT NULL
        )
        """)

        # =========================================================
        # TABLA ENVIOS
        # =========================================================
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS envios (
            id_envio INTEGER PRIMARY KEY AUTOINCREMENT,
            id_cliente INTEGER NOT NULL,
            id_paquete INTEGER NOT NULL,
            id_destino INTEGER NOT NULL,
            fecha_envio TEXT NOT NULL,
            estado_envio TEXT NOT NULL,
            FOREIGN KEY(id_cliente) REFERENCES clientes(id_cliente),
            FOREIGN KEY(id_paquete) REFERENCES paquetes(id_paquete),
            FOREIGN KEY(id_destino) REFERENCES destinos(id_destino)
        )
        """)

        # =========================================================
        # CARGA CLIENTES
        # =========================================================
        cursor.execute("SELECT COUNT(*) FROM clientes")
        if cursor.fetchone()[0] == 0:
            df_clientes = pd.read_csv(io.StringIO(csv_clientes))
            df_clientes.to_sql("clientes", conn, if_exists="append", index=False)

        # =========================================================
        # CARGA PAQUETES
        # =========================================================
        cursor.execute("SELECT COUNT(*) FROM paquetes")
        if cursor.fetchone()[0] == 0:
            df_paquetes = pd.read_csv(io.StringIO(csv_paquetes))
            df_paquetes.to_sql("paquetes", conn, if_exists="append", index=False)

        # =========================================================
        # CARGA DESTINOS
        # =========================================================
        cursor.execute("SELECT COUNT(*) FROM destinos")
        if cursor.fetchone()[0] == 0:
            df_destinos = pd.read_csv(io.StringIO(csv_destinos))
            df_destinos.to_sql("destinos", conn, if_exists="append", index=False)

        # =========================================================
        # CARGA ENVIOS
        # =========================================================
        cursor.execute("SELECT COUNT(*) FROM envios")
        if cursor.fetchone()[0] == 0:
            df_envios = pd.read_csv(io.StringIO(csv_envios))
            df_envios.to_sql("envios", conn, if_exists="append", index=False)

        conn.commit()

    print("Base de datos Meta-Logística cargada correctamente.")

# =========================================================
# EJECUCIÓN PRINCIPAL
# =========================================================
if __name__ == "__main__":
    cargar_db()
    root = tk.Tk()
    app = AppCentral(root, DB_NAME)
    root.mainloop()
