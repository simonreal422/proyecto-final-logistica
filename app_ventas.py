import tkinter as tk
from tkinter import ttk, messagebox

from ventas import EnvioManager


class PantallaEnvios:

    def __init__(self, db_name):

        self.manager = EnvioManager(db_name)

        self.window = tk.Toplevel()

        self.window.title("Envíos")

        self.window.geometry("600x400")

        tk.Label(self.window, text="ID Cliente").pack()
        self.entry_cliente = tk.Entry(self.window)
        self.entry_cliente.pack()

        tk.Label(self.window, text="ID Paquete").pack()
        self.entry_paquete = tk.Entry(self.window)
        self.entry_paquete.pack()

        tk.Label(self.window, text="ID Destino").pack()
        self.entry_destino = tk.Entry(self.window)
        self.entry_destino.pack()

        tk.Label(self.window, text="Estado Envío").pack()
        self.entry_estado = tk.Entry(self.window)
        self.entry_estado.pack()

        ttk.Button(
            self.window,
            text="Registrar Envío",
            command=self.registrar
        ).pack(pady=10)

    def registrar(self):

        try:

            self.manager.create(
                int(self.entry_cliente.get()),
                int(self.entry_paquete.get()),
                int(self.entry_destino.get()),
                self.entry_estado.get()
            )

            messagebox.showinfo(
                "Éxito",
                "Envío registrado"
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )