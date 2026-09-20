# Restaurante App - Semana 14

## 🎯 Propósito
La actividad de la **Semana 14** tiene como objetivo aplicar correctamente **componentes y contenedores en Tkinter**, manteniendo la arquitectura modular del proyecto y mejorando la interfaz gráfica.  
Las operaciones sobre productos sirven como contexto práctico para demostrar la integración de formularios, tablas y botones en la aplicación.

---

## 📂 Estructura del proyecto
restaurante_app/
├── datos/
│   ├── productos.json
│   └── usuarios.json
├── modelos/
│   └── producto.py
├── servicios/
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── login_view.py
│   └── main_view.py
├── assets/                  (opcional, recursos visuales)
├── main.py
└── README.md

---

## 🧩 Componentes y contenedores utilizados
- **Contenedores (Frames, LabelFrame)**: separación de zonas de navegación, formulario y tabla de datos.
- **Componentes de Tkinter**:
  - `Entry` para captura de datos (código, nombre, categoría, precio, stock).
  - `Button` con `command=` para ejecutar operaciones.
  - `Treeview` de `ttk` para mostrar productos y usuarios en tabla.
  - `Label` para identificar campos en el formulario.

---

## ✨ Mejoras realizadas en la interfaz
- Separación clara entre **navegación lateral** y **contenido principal**.
- Inclusión de un **formulario de gestión de productos** con campos organizados.
- Tabla interactiva (`Treeview`) para visualizar usuarios y productos.
- Actualización automática de la interfaz después de cada operación.
- Mensajes de confirmación y error para mejorar la experiencia del usuario.

---

## 🛠️ Operaciones implementadas sobre productos
- **Registrar**: agrega un nuevo producto validando que no exista previamente.
- **Consultar/Cargar**: muestra todos los productos en la tabla.
- **Actualizar**: modifica nombre, categoría, precio y stock de un producto existente.
- **Eliminar**: borra un producto identificado por su código.

---

## 💾 Persistencia utilizada
- Los datos se almacenan en archivos **JSON** dentro de la carpeta `datos/`.
- `productos.json` guarda la información de los productos.
- `usuarios.json` contiene credenciales y datos de usuarios.
- La clase `RestauranteServicio` gestiona la lectura y escritura mediante `archivo_servicio`.

---

## 🚀 Pasos para ejecutar `main.py`
1. Clonar o descargar el proyecto.
2. Verificar que esté instalado **Python 3.10+**.
3. Abrir una terminal en la carpeta raíz del proyecto.
4. Ejecutar:
   ```bash
   python main.py
