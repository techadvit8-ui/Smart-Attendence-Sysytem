import customtkinter as ctk
from tkinter import messagebox
from database.database import Database


class RegisterStudentPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.db = Database()

        title = ctk.CTkLabel(
            self,
            text="Student Registration",
            font=("Segoe UI", 28, "bold")
        )
        title.pack(pady=20)

        form = ctk.CTkFrame(self)
        form.pack(pady=10, padx=20)

        # Name
        ctk.CTkLabel(form, text="Student Name").grid(row=0, column=0, padx=15, pady=10, sticky="w")
        self.name = ctk.CTkEntry(form, width=300)
        self.name.grid(row=0, column=1, pady=10)

        # Roll Number
        ctk.CTkLabel(form, text="Roll Number").grid(row=1, column=0, padx=15, pady=10, sticky="w")
        self.roll = ctk.CTkEntry(form, width=300)
        self.roll.grid(row=1, column=1)

        # Class
        ctk.CTkLabel(form, text="Class").grid(row=2, column=0, padx=15, pady=10, sticky="w")
        self.student_class = ctk.CTkEntry(form, width=300)
        self.student_class.grid(row=2, column=1)

        # Section
        ctk.CTkLabel(form, text="Section").grid(row=3, column=0, padx=15, pady=10, sticky="w")
        self.section = ctk.CTkEntry(form, width=300)
        self.section.grid(row=3, column=1)

        # Parent Mobile
        ctk.CTkLabel(form, text="Parent Mobile").grid(row=4, column=0, padx=15, pady=10, sticky="w")
        self.mobile = ctk.CTkEntry(form, width=300)
        self.mobile.grid(row=4, column=1)

        # Email
        ctk.CTkLabel(form, text="Email").grid(row=5, column=0, padx=15, pady=10, sticky="w")
        self.email = ctk.CTkEntry(form, width=300)
        self.email.grid(row=5, column=1)

        # Buttons
        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.pack(pady=20)

        save_btn = ctk.CTkButton(
            button_frame,
            text="💾 Save",
            width=150,
            command=self.save_student
        )
        save_btn.pack(side="left", padx=10)

        clear_btn = ctk.CTkButton(
            button_frame,
            text="🗑 Clear",
            width=150,
            fg_color="red",
            hover_color="#8B0000",
            command=self.clear_form
        )
        clear_btn.pack(side="left", padx=10)

    def save_student(self):

        name = self.name.get().strip()
        roll = self.roll.get().strip()
        student_class = self.student_class.get().strip()
        section = self.section.get().strip()
        mobile = self.mobile.get().strip()
        email = self.email.get().strip()

        if name == "" or roll == "":
            messagebox.showerror(
                "Error",
                "Name and Roll Number are required."
            )
            return

        image_path = f"datasets/{name}/face.jpg"

        try:
            self.db.add_student(
                name,
                roll,
                student_class,
                section,
                mobile,
                email,
                image_path
            )

            messagebox.showinfo(
                "Success",
                "Student Registered Successfully!"
            )

            self.clear_form()

        except Exception as e:
            messagebox.showerror(
                "Database Error",
                str(e)
            )

    def clear_form(self):

        self.name.delete(0, "end")
        self.roll.delete(0, "end")
        self.student_class.delete(0, "end")
        self.section.delete(0, "end")
        self.mobile.delete(0, "end")
        self.email.delete(0, "end")