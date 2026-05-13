import tkinter as tk
from tkinter import ttk, messagebox

from productos import PaqueteManager


class PantallaPaquetes:

    def __init__(self, db_name):

        self.manager = PaqueteManager(db_name)

        self.window = tk.Toplevel()

        self.window.title("Gestión de Paquetes")

        self.window.geometry("700x500")

        tk.Label(self.window, text="ID Paquete").pack()
        self.entry_id = tk.Entry(self.window)
        self.entry_id.pack()

        tk.Label(self.window, text="Peso (kg)").pack()
        self.entry_peso = tk.Entry(self.window)
        self.entry_peso.pack()

        tk.Label(self.window, text="Destino").pack()
        self.entry_destino = tk.Entry(self.window)
        self.entry_destino.pack()

        tk.Label(self.window, text="Estado").pack()
        self.entry_estado = tk.Entry(self.window)
        self.entry_estado.pack()

        ttk.Button(
            self.window,
            text="Registrar Paquete",
            command=self.registrar
        ).pack(pady=10)

        ttk.Button(
            self.window,
            text="Limpiar",
            command=self.limpiar
        ).pack(pady=10)

    def registrar(self):

        try:

            id_paquete = int(self.entry_id.get())

            peso = float(self.entry_peso.get())

            destino = self.entry_destino.get()

            estado = self.entry_estado.get()

            self.manager.create(
                id_paquete,
                peso,
                destino,
                estado
            )

            messagebox.showinfo(
                "Éxito",
                "Paquete registrado correctamente"
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    def limpiar(self):

        self.entry_id.delete(0, tk.END)

        self.entry_peso.delete(0, tk.END)

        self.entry_destino.delete(0, tk.END)

        self.entry_estado.delete(0, tk.END)