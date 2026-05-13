import tkinter as tk
from tkinter import ttk

from app_clientes import PantallaClientes
from app_productos import PantallaPaquetes
from app_proveedores import PantallaDestinos
from app_ventas import PantallaEnvios


class AppCentral:

    def __init__(self, root, db_name):

        self.root = root
        self.db_name = db_name

        self.root.title("Meta-Logística S.A.S.")
        self.root.geometry("600x400")

        titulo = tk.Label(
            root,
            text="🚚 META-LOGÍSTICA S.A.S.",
            font=("Arial", 18, "bold")
        )

        titulo.pack(pady=20)

        ttk.Button(
            root,
            text="👥 Módulo Clientes",
            command=self.abrir_clientes
        ).pack(pady=10)

        ttk.Button(
            root,
            text="📦 Módulo Paquetes",
            command=self.abrir_paquetes
        ).pack(pady=10)

        ttk.Button(
            root,
            text="📍 Módulo Destinos",
            command=self.abrir_destinos
        ).pack(pady=10)

        ttk.Button(
            root,
            text="🚛 Módulo Envíos",
            command=self.abrir_envios
        ).pack(pady=10)

    def abrir_clientes(self):

        PantallaClientes(self.db_name)

    def abrir_paquetes(self):

        PantallaPaquetes(self.db_name)

    def abrir_destinos(self):

        PantallaDestinos(self.db_name)

    def abrir_envios(self):

        PantallaEnvios(self.db_name)