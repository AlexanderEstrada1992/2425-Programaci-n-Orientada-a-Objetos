import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
root = tk.Tk()
root.title("Gestión de Tareas")

# Crear una lista de tareas
tasks = []

# Función para agregar una tarea
def add_task():
    task = task_entry.get()  # Obtener el texto del campo de entrada
    if task:  # Si la tarea no está vacía
        tasks.append(task)  # Añadir la tarea a la lista
        update_task_list()  # Actualizar la lista visual
        task_entry.delete(0, tk.END)  # Limpiar el campo de entrada
    else:
        messagebox.showwarning("Entrada vacía", "Por favor ingrese una tarea.")

# Función para marcar una tarea como completada
def mark_completed():
    try:
        selected_task_index = task_list.curselection()[0]  # Obtener la tarea seleccionada
        task_list.itemconfig(selected_task_index, {'bg': 'light green'})  # Cambiar color de fondo para completada
        tasks[selected_task_index] += " (Completada)"  # Agregar "(Completada)" al texto de la tarea
    except IndexError:
        messagebox.showwarning("No seleccionada", "Por favor, seleccione una tarea para marcar como completada.")

# Función para eliminar una tarea
def delete_task():
    try:
        selected_task_index = task_list.curselection()[0]  # Obtener la tarea seleccionada
        del tasks[selected_task_index]  # Eliminar la tarea de la lista
        update_task_list()  # Actualizar la lista visual
    except IndexError:
        messagebox.showwarning("No seleccionada", "Por favor, seleccione una tarea para eliminar.")

# Función para actualizar la lista de tareas visualmente
def update_task_list():
    task_list.delete(0, tk.END)  # Limpiar la lista actual
    for task in tasks:  # Recorrer todas las tareas
        task_list.insert(tk.END, task)  # Insertar cada tarea en la lista

# Función para cerrar la aplicación con "Escape"
def close_app(event=None):
    root.quit()

# Crear los widgets para la interfaz
task_entry = tk.Entry(root, width=40)  # Campo de entrada para nueva tarea
add_button = tk.Button(root, text="Añadir Tarea", command=add_task)  # Botón para agregar tarea
complete_button = tk.Button(root, text="Marcar como Completada", command=mark_completed)  # Botón para marcar como completada
delete_button = tk.Button(root, text="Eliminar Tarea", command=delete_task)  # Botón para eliminar tarea

# Crear una lista para mostrar las tareas
task_list = tk.Listbox(root, width=50, height=10, selectmode=tk.SINGLE)

# Posicionar los widgets en la ventana utilizando grid
task_entry.grid(row=0, column=0, padx=10, pady=10)
add_button.grid(row=0, column=1, padx=10, pady=10)
task_list.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
complete_button.grid(row=2, column=0, padx=10, pady=10)
delete_button.grid(row=2, column=1, padx=10, pady=10)

# Funciones de atajos de teclado
root.bind('<Return>', lambda event: add_task())  # Tecla "Enter" para agregar tarea
root.bind('<c>', lambda event: mark_completed())  # Tecla "C" para marcar como completada
root.bind('<Delete>', lambda event: delete_task())  # Tecla "Delete" para eliminar tarea
root.bind('<Escape>', close_app)  # Tecla "Escape" para cerrar la aplicación

# Iniciar la aplicación
root.mainloop()
