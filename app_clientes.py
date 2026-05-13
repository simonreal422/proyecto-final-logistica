import tkinter as tk
from tkinter import ttk, messagebox

from clientes import ClienteManager


class PantallaClientes:

    def __init__(self, db_name):

        self.manager = ClienteManager(db_name)

        self.window = tk.Toplevel()

        self.window.title("Gestión Clientes")

        self.window.geometry("700x500")

        tk.Label(self.window, text="ID Cliente").pack()
        self.entry_id = tk.Entry(self.window)
        self.entry_id.pack()

        tk.Label(self.window, text="Email").pack()
        self.entry_email = tk.Entry(self.window)
        self.entry_email.pack()

        tk.Label(self.window, text="Teléfono").pack()
        self.entry_telefono = tk.Entry(self.window)
        self.entry_telefono.pack()

        tk.Label(self.window, text="Fecha Nacimiento").pack()
        self.entry_fecha = tk.Entry(self.window)
        self.entry_fecha.pack()

        tk.Label(self.window, text="Nombre").pack()
        self.entry_nombre = tk.Entry(self.window)
        self.entry_nombre.pack()

        tk.Label(self.window, text="Tipo Cliente").pack()
        self.entry_tipo = tk.Entry(self.window)
        self.entry_tipo.pack()

        ttk.Button(
            self.window,
            text="Registrar Cliente",
            command=self.registrar
        ).pack(pady=10)

    def registrar(self):

        try:

            self.manager.create(
                int(self.entry_id.get()),
                self.entry_email.get(),
                self.entry_telefono.get(),
                self.entry_fecha.get(),
                self.entry_nombre.get(),
                self.entry_tipo.get()
            )

            messagebox.showinfo(
                "Éxito",
                "Cliente registrado"
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )