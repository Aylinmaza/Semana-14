import tkinter as tk
from tkinter import messagebox

class LoginView(tk.Frame):
    def __init__(self, master, servicio, on_login_success):
        super().__init__(master)
        self.servicio = servicio
        self.on_login_success = on_login_success

        tk.Label(self, text="Usuario:").pack(pady=5)
        self.entry_usuario = tk.Entry(self)
        self.entry_usuario.pack(pady=5)

        tk.Label(self, text="Contraseña:").pack(pady=5)
        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.pack(pady=5)

        tk.Button(self, text="Ingresar", command=self.validar).pack(pady=10)

    def validar(self):
        usuario = self.entry_usuario.get()
        password = self.entry_password.get()

        print("Ingresado en login -> Usuario:", usuario, "Password:", password)

        # Advertencia si los campos están vacíos
        if not usuario or not password:
            messagebox.showerror("Error", "Debe ingresar usuario y contraseña")
            return

        # Validación contra usuarios cargados
        if self.servicio.validar_acceso(usuario, password):
            print("Acceso concedido")
            messagebox.showinfo("Bienvenido", f"Acceso concedido a {usuario}")
            self.on_login_success()
        else:
            print("Acceso denegado: no coincide con usuarios cargados")
            messagebox.showerror("Acceso denegado", "Credenciales incorrectas")