#  Desarrollar una aplicación GUI simple para gestionar una lista de tareas, permitiendo al usuario añadir nuevas tareas, marcarlas como completadas y eliminarlas.
#  La aplicación deberá responder adecuadamente a los eventos del usuario, como clics del ratón y pulsaciones del teclado.
import tkinter as tk
from tkinter import messagebox

def add_task(event=None):
    task = task_entry.get().strip()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "La tarea no puede estar vacía")

def mark_completed():
    try:
        selected_index = task_listbox.curselection()[0]
        task = task_listbox.get(selected_index)
        task_listbox.delete(selected_index)
        task_listbox.insert(selected_index, f"✔ {task}")
    except IndexError:
        messagebox.showwarning("Advertencia", "Seleccione una tarea para marcar como completada")

def delete_task():
    try:
        selected_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Advertencia", "Seleccione una tarea para eliminar")

# Crear ventana principal
root = tk.Tk()
root.title("Gestor de Tareas")
root.geometry("400x400")

# Campo de entrada de tarea
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)
task_entry.bind("<Return>", add_task)  # Permitir añadir con Enter

# Botones
add_button = tk.Button(root, text="Añadir Tarea", command=add_task)
add_button.pack(pady=5)

mark_button = tk.Button(root, text="Marcar como Completada", command=mark_completed)
mark_button.pack(pady=5)

delete_button = tk.Button(root, text="Eliminar Tarea", command=delete_task)
delete_button.pack(pady=5)

# Lista de tareas
task_listbox = tk.Listbox(root, width=50, height=15)
task_listbox.pack(pady=10)

# Iniciar aplicación
root.mainloop()
