# Desarrollar una aplicación GUI utilizando Tkinter en Python que funcione como una agenda personal.
# La aplicación permitirá al usuario agregar, ver, y eliminar eventos o tareas programadas.
import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

def agregar_evento():
    fecha = entry_fecha.get()
    hora = entry_hora.get()
    descripcion = entry_descripcion.get()
    if fecha and hora and descripcion:
        tree.insert("", "end", values=(fecha, hora, descripcion))
        entry_fecha.set_date('')
        entry_hora.delete(0, tk.END)
        entry_descripcion.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada inválida", "Todos los campos son obligatorios")

def eliminar_evento():
    selected_item = tree.selection()
    if selected_item:
        confirm = messagebox.askyesno("Confirmar eliminación", "¿Deseas eliminar el evento seleccionado?")
        if confirm:
            tree.delete(selected_item)
    else:
        messagebox.showwarning("Selección inválida", "Selecciona un evento para eliminar")

def salir():
    root.quit()

# Configuración de la ventana principal
root = tk.Tk()
root.title("Nueva Agenda Personal")
root.geometry("500x400")

# Frame para la entrada de datos
frame_input = ttk.Frame(root, padding="10")
frame_input.pack(fill='x')

ttk.Label(frame_input, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
entry_fecha = DateEntry(frame_input, width=12, background='darkblue', foreground='white', borderwidth=2)
entry_fecha.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame_input, text="Hora:").grid(row=1, column=0, padx=5, pady=5)
entry_hora = ttk.Entry(frame_input)
entry_hora.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(frame_input, text="Descripción:").grid(row=2, column=0, padx=5, pady=5)
entry_descripcion = ttk.Entry(frame_input)
entry_descripcion.grid(row=2, column=1, padx=5, pady=5)

# Botones
frame_buttons = ttk.Frame(root, padding="10")
frame_buttons.pack(fill='x')

ttk.Button(frame_buttons, text="Agregar Evento", command=agregar_evento).pack(side='left', padx=5)
ttk.Button(frame_buttons, text="Eliminar Evento Seleccionado", command=eliminar_evento).pack(side='left', padx=5)
ttk.Button(frame_buttons, text="Salir", command=salir).pack(side='right', padx=5)

# Lista de eventos (TreeView)
frame_list = ttk.Frame(root, padding="10")
frame_list.pack(fill='both', expand=True)

tree = ttk.Treeview(frame_list, columns=("Fecha", "Hora", "Descripción"), show='headings')
tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción", text="Descripción")
tree.pack(fill='both', expand=True)

root.mainloop()