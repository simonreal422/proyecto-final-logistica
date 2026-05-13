import tkinter as tk
from tkinter import ttk, messagebox

from proveedores import DestinoManager


class PantallaDestinos:

    def __init__(self, db_name):

        self.manager = DestinoManager(db_name)

        self.window = tk.Toplevel()

        self.window.title("Destinos")

        self.window.geometry("600x400")

        tk.Label(self.window, text="ID Destino").pack()
        self.entry_id = tk.Entry(self.window)
        self.entry_id.pack()

        tk.Label(self.window, text="Ciudad").pack()
        self.entry_ciudad = tk.Entry(self.window)
        self.entry_ciudad.pack()

        tk.Label(self.window, text="Departamento").pack()
        self.entry_departamento = tk.Entry(self.window)
        self.entry_departamento.pack()

        tk.Label(self.window, text="Zona").pack()
        self.entry_zona = tk.Entry(self.window)
        self.entry_zona.pack()

        ttk.Button(
            self.window,
            text="Registrar Destino",
            command=self.registrar
        ).pack(pady=10)

    def registrar(self):

        try:

            self.manager.create(
                int(self.entry_id.get()),
                self.entry_ciudad.get(),
                self.entry_departamento.get(),
                self.entry_zona.get()
            )

            messagebox.showinfo(
                "Éxito",
                "Destino registrado"
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )