import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry


class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("500x400")

        # Frame para ingresar datos
        frame_input = tk.Frame(self.root, padx=10, pady=10)
        frame_input.pack(fill=tk.X)

        tk.Label(frame_input, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
        self.date_entry = DateEntry(frame_input, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_input, text="Hora:").grid(row=1, column=0, padx=5, pady=5)
        self.time_entry = tk.Entry(frame_input, width=15)
        self.time_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame_input, text="Descripción:").grid(row=2, column=0, padx=5, pady=5)
        self.desc_entry = tk.Entry(frame_input, width=30)
        self.desc_entry.grid(row=2, column=1, padx=5, pady=5)

        # Botón para agregar evento
        self.add_button = tk.Button(frame_input, text="Agregar Evento", command=self.add_event)
        self.add_button.grid(row=3, columnspan=2, pady=10)

        # Frame para mostrar la lista de eventos
        frame_list = tk.Frame(self.root)
        frame_list.pack(fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(frame_list, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Botón para eliminar evento
        self.delete_button = tk.Button(self.root, text="Eliminar Evento", command=self.delete_event)
        self.delete_button.pack(pady=5)

        # Botón para salir
        self.exit_button = tk.Button(self.root, text="Salir", command=self.root.quit)
        self.exit_button.pack(pady=5)

    def add_event(self):
        date = self.date_entry.get()
        time = self.time_entry.get()
        description = self.desc_entry.get()

        if date and time and description:
            self.tree.insert("", tk.END, values=(date, time, description))
            self.time_entry.delete(0, tk.END)
            self.desc_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos")

    def delete_event(self):
        selected_item = self.tree.selection()
        if selected_item:
            confirm = messagebox.askyesno("Confirmación", "¿Está seguro de eliminar el evento seleccionado?")
            if confirm:
                self.tree.delete(selected_item)
        else:
            messagebox.showwarning("Advertencia", "Seleccione un evento para eliminar")


if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
