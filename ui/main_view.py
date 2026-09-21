import tkinter as tk
from tkinter import ttk, messagebox

class MainView(tk.Frame):
    def __init__(self, master, servicio, on_logout):
        super().__init__(master)
        self.servicio = servicio
        self.on_logout = on_logout
        self.pack(fill="both", expand=True)

        # --- Navegación ---
        nav_frame = tk.Frame(self, bd=2, relief="groove")
        nav_frame.pack(side="left", fill="y", padx=10, pady=10)

        tk.Button(nav_frame, text="Usuarios", command=self.mostrar_usuarios).pack(pady=5, fill="x")
        tk.Button(nav_frame, text="Productos", command=self.mostrar_productos).pack(pady=5, fill="x")
        tk.Button(nav_frame, text="Cerrar sesión", command=self.on_logout).pack(pady=20, fill="x")

        # --- Contenido ---
        content_frame = tk.Frame(self, bd=2, relief="groove")
        content_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        # Tabla
        self.tree = ttk.Treeview(content_frame, columns=("codigo","nombre","categoria","precio","stock"), show="headings")
        for col in ("codigo","nombre","categoria","precio","stock"):
            self.tree.heading(col, text=col.capitalize())
            self.tree.column(col, width=100)
        self.tree.pack(fill="both", expand=True)

        # Vincular selección de fila
        self.tree.bind("<<TreeviewSelect>>", self.seleccionar_producto)

        # Formulario
        form_frame = tk.LabelFrame(content_frame, text="Gestión de productos")
        form_frame.pack(fill="x", pady=10)

        campos = [("codigo","Código"), ("nombre","Nombre"), ("categoria","Categoría"), ("precio","Precio"), ("stock","Stock")]
        self.entries = {}
        for i, (key, label) in enumerate(campos):
            tk.Label(form_frame, text=label+":").grid(row=i, column=0, sticky="w")
            entry = tk.Entry(form_frame)
            entry.grid(row=i, column=1, padx=5, pady=2)
            self.entries[key] = entry

        tk.Button(form_frame, text="Registrar", command=self.registrar_producto).grid(row=5, column=0, pady=5)
        tk.Button(form_frame, text="Actualizar", command=self.actualizar_producto).grid(row=5, column=1, pady=5)
        tk.Button(form_frame, text="Eliminar", command=self.eliminar_producto).grid(row=5, column=2, pady=5)

    # --- Métodos ---
    def mostrar_usuarios(self):
        usuarios = self.servicio.listar_usuarios()
        self.tree.delete(*self.tree.get_children())
        for u in usuarios:
            self.tree.insert("", tk.END, values=(u["identificacion"], u["nombre"], u["rol"], "-", "-"))

    def mostrar_productos(self):
        productos = self.servicio.listar_productos()
        self.tree.delete(*self.tree.get_children())
        for p in productos:
            self.tree.insert("", tk.END, values=(p.codigo, p.nombre, p.categoria, p.precio, p.stock))

    def registrar_producto(self):
        try:
            self.servicio.registrar_producto(
                self.entries["codigo"].get(),
                self.entries["nombre"].get(),
                self.entries["categoria"].get(),
                self.entries["precio"].get(),
                self.entries["stock"].get()
            )
            messagebox.showinfo("Éxito", "Producto registrado correctamente")
            self.mostrar_productos()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def actualizar_producto(self):
        try:
            self.servicio.actualizar_producto(
                self.entries["codigo"].get(),
                self.entries["nombre"].get(),
                self.entries["categoria"].get(),
                self.entries["precio"].get(),
                self.entries["stock"].get()
            )
            messagebox.showinfo("Éxito", "Producto actualizado correctamente")
            self.mostrar_productos()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def eliminar_producto(self):
        try:
            self.servicio.eliminar_producto(self.entries["codigo"].get())
            messagebox.showinfo("Éxito", "Producto eliminado correctamente")
            self.mostrar_productos()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def seleccionar_producto(self, event):
        """Cuando seleccionas una fila en la tabla, llena los campos del formulario."""
        seleccion = self.tree.selection()
        if seleccion:
            valores = self.tree.item(seleccion[0], "values")
            keys = ["codigo","nombre","categoria","precio","stock"]
            for k, v in zip(keys, valores):
                self.entries[k].delete(0, tk.END)
                self.entries[k].insert(0, v)
