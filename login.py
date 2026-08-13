import customtkinter as ctk
from tkinter import messagebox

from gui.dashboard import Dashboard


class LoginWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Smart Attendance System - Login")
        self.geometry("1000x600")
        self.resizable(False, False)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.center_window()

        # ---------------- Left Panel ---------------- #

        left = ctk.CTkFrame(self, width=450, corner_radius=0)
        left.pack(side="left", fill="y")

        ctk.CTkLabel(
            left,
            text="Smart Attendance\nSystem",
            font=("Segoe UI", 30, "bold")
        ).pack(pady=(120, 10))

        ctk.CTkLabel(
            left,
            text="AI Powered Face Recognition",
            font=("Segoe UI", 18)
        ).pack()

        ctk.CTkLabel(
            left,
            text="Secure • Fast • Reliable",
            font=("Segoe UI", 14)
        ).pack(pady=20)

        # ---------------- Right Panel ---------------- #

        right = ctk.CTkFrame(self, fg_color="transparent")
        right.pack(side="right", expand=True, fill="both")

        ctk.CTkLabel(
            right,
            text="Administrator Login",
            font=("Segoe UI", 26, "bold")
        ).pack(pady=(80, 30))

        self.username = ctk.CTkEntry(
            right,
            width=320,
            height=40,
            placeholder_text="Username"
        )
        self.username.pack(pady=10)

        self.password = ctk.CTkEntry(
            right,
            width=320,
            height=40,
            placeholder_text="Password",
            show="*"
        )
        self.password.pack(pady=10)

        self.show_var = ctk.BooleanVar()

        show = ctk.CTkCheckBox(
            right,
            text="Show Password",
            variable=self.show_var,
            command=self.toggle_password
        )
        show.pack(pady=5)

        self.remember = ctk.BooleanVar()

        remember = ctk.CTkCheckBox(
            right,
            text="Remember Me",
            variable=self.remember
        )
        remember.pack()

        ctk.CTkButton(
            right,
            text="Login",
            width=320,
            height=40,
            command=self.login
        ).pack(pady=(30, 10))

        ctk.CTkButton(
            right,
            text="Exit",
            width=320,
            height=40,
            fg_color="red",
            hover_color="darkred",
            command=self.destroy
        ).pack()

        ctk.CTkLabel(
            right,
            text="Version 1.0",
            font=("Segoe UI", 12)
        ).pack(side="bottom", pady=20)

    def toggle_password(self):
        if self.show_var.get():
            self.password.configure(show="")
        else:
            self.password.configure(show="*")

    def login(self):

        username = self.username.get()
        password = self.password.get()

        if username == "admin" and password == "admin123":
            messagebox.showinfo(
                "Success",
                "Login Successful!"
            )

            # Dashboard will open here later

            self.destroy()
            from gui.dashboard import Dashboard

            dashboard = Dashboard()
            dashboard.mainloop()
            

        else:
            messagebox.showerror(
                "Error",
                "Invalid Username or Password"
            )

    def center_window(self):

        width = 1000
        height = 600

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = int((screen_width-width)/2)
        y = int((screen_height-height)/2)

        self.geometry(f"{width}x{height}+{x}+{y}")


if __name__ == "__main__":
    app = LoginWindow()
    app.mainloop()