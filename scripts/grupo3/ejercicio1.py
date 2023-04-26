"""
Make a window, where you can fill in a record of a student (Name, age, course)
 and when displayed, you can see it in the table.
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class StudentRecordApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Registro de estudiantes")
        self.create_widgets()

    def create_widgets(self):
        # Create the student record entry form
        self.record_frame = ttk.LabelFrame(self.master,
                                           text="Formulario de registro")
        self.record_frame.grid(row=0,
                               column=0,
                               padx=10,
                               pady=10,
                               sticky="nsew")

        # Student Name label and entry
        self.name_label = ttk.Label(self.record_frame, text="Nombre:")
        self.name_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.name_entry = ttk.Entry(self.record_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        # Student Age label and entry
        self.age_label = ttk.Label(self.record_frame, text="Edad:")
        self.age_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.age_entry = ttk.Entry(self.record_frame)
        self.age_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        # Student Course label and entry
        self.course_label = ttk.Label(self.record_frame, text="Curso:")
        self.course_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.course_entry = ttk.Entry(self.record_frame)
        self.course_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        # Submit button
        self.submit_button = ttk.Button(self.record_frame,
                                        text="Guardar",
                                        command=self.submit_record)
        self.submit_button.grid(row=3,
                                column=1,
                                padx=5,
                                pady=5,
                                sticky="w",
                               )

        # Create the student record table
        self.table_frame = ttk.LabelFrame(self.master,
                                          text="Tabla de registros")
        self.table_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.treeview = ttk.Treeview(self.table_frame,
                                     columns=("name", "age", "course"))
        self.treeview.heading("#0", text="ID")
        self.treeview.heading("name", text="Nombre")
        self.treeview.heading("age", text="Edad")
        self.treeview.heading("course", text="Curso")
        self.treeview.pack(side="left", fill="both", expand=True)

    def submit_record(self):
        # Get the student record data from the entry form
        name = self.name_entry.get()
        age = self.age_entry.get()
        course = self.course_entry.get()

        if not name or not age or not course:
            messagebox.showerror("Error",
                                 "Por favor, rellene todos los campos")
            return

        # Insert the student record data into the table
        id = len(self.treeview.get_children()) + 1
        self.treeview.insert("", "end", text=id, values=(name, age, course))

        # Clear the student record entry form
        self.name_entry.delete(0, "end")
        self.age_entry.delete(0, "end")
        self.course_entry.delete(0, "end")


if __name__ == "__main__":
    root = tk.Tk()
    app = StudentRecordApp(root)
    root.mainloop()
