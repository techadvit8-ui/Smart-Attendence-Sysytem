import customtkinter as ctk
from datetime import datetime

from gui.pages.register_student import RegisterStudentPage


ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class Dashboard(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Smart Attendance System")
        self.geometry("1500x850")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.create_sidebar()
        self.create_main()

        self.update_clock()

    # -----------------------------
    # Sidebar
    # -----------------------------

    def create_sidebar(self):

        self.sidebar = ctk.CTkFrame(self, width=250)
        self.sidebar.grid(row=0, column=0, sticky="ns")

        title = ctk.CTkLabel(
            self.sidebar,
            text="SMART\nATTENDANCE",
            font=("Segoe UI", 28, "bold")
        )
        title.pack(pady=25)

        ctk.CTkButton(
            self.sidebar,
            text="🏠 Dashboard",
            command=self.show_dashboard
        ).pack(fill="x", padx=20, pady=8)

        ctk.CTkButton(
            self.sidebar,
            text="👤 Register Student",
            command=self.show_register
        ).pack(fill="x", padx=20, pady=8)

        ctk.CTkButton(
            self.sidebar,
            text="📷 Live Recognition",
            command=self.show_camera
        ).pack(fill="x", padx=20, pady=8)

        ctk.CTkButton(
            self.sidebar,
            text="📋 Attendance",
            command=self.show_attendance
        ).pack(fill="x", padx=20, pady=8)

        ctk.CTkButton(
            self.sidebar,
            text="📊 Reports",
            command=self.show_reports
        ).pack(fill="x", padx=20, pady=8)

        ctk.CTkButton(
            self.sidebar,
            text="⚙ Settings"
        ).pack(fill="x", padx=20, pady=8)

        ctk.CTkButton(
            self.sidebar,
            text="❌ Exit",
            fg_color="red",
            command=self.destroy
        ).pack(side="bottom", padx=20, pady=20, fill="x")

    # -----------------------------
    # Main Area
    # -----------------------------

    def create_main(self):

        self.main = ctk.CTkFrame(self)
        self.main.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        self.show_dashboard()

    # -----------------------------
    # Dashboard Home
    # -----------------------------

    def show_dashboard(self):

        for widget in self.main.winfo_children():
            widget.destroy()

        header = ctk.CTkLabel(
            self.main,
            text="Dashboard",
            font=("Segoe UI", 30, "bold")
        )
        header.pack(pady=15)

        self.clock = ctk.CTkLabel(
            self.main,
            text="",
            font=("Segoe UI", 18)
        )
        self.clock.pack()

        cards = ctk.CTkFrame(self.main)
        cards.pack(pady=20)

        self.create_card(cards, "👨 Students", "4").grid(row=0, column=0, padx=15)
        self.create_card(cards, "✅ Present", "0").grid(row=0, column=1, padx=15)
        self.create_card(cards, "❌ Absent", "4").grid(row=0, column=2, padx=15)
        self.create_card(cards, "⚠ Unknown", "0").grid(row=0, column=3, padx=15)

        camera = ctk.CTkFrame(self.main, width=700, height=400)
        camera.pack(pady=20)

        camera.pack_propagate(False)

        ctk.CTkLabel(
            camera,
            text="📷 Live Camera Preview",
            font=("Segoe UI", 24)
        ).pack(expand=True)

    # -----------------------------

    def create_card(self, parent, title, value):

        frame = ctk.CTkFrame(parent, width=180, height=120)

        frame.pack_propagate(False)

        ctk.CTkLabel(
            frame,
            text=title,
            font=("Segoe UI", 18)
        ).pack(pady=10)

        ctk.CTkLabel(
            frame,
            text=value,
            font=("Segoe UI", 30, "bold")
        ).pack()

        return frame

    # -----------------------------
    # Register Student
    # -----------------------------

    def show_register(self):

        for widget in self.main.winfo_children():
            widget.destroy()

        RegisterStudentPage(self.main).pack(
            fill="both",
            expand=True
        )

    # -----------------------------
    # Live Recognition
    # -----------------------------

    def show_camera(self):

        for widget in self.main.winfo_children():
            widget.destroy()

        ctk.CTkLabel(
            self.main,
            text="📷 Live Recognition",
            font=("Segoe UI", 30, "bold")
        ).pack(pady=20)

        ctk.CTkLabel(
            self.main,
            text="Connect LiveRecognition widget here.",
            font=("Segoe UI", 18)
        ).pack()

    # -----------------------------
    # Attendance
    # -----------------------------

    def show_attendance(self):

        for widget in self.main.winfo_children():
            widget.destroy()

        ctk.CTkLabel(
            self.main,
            text="Attendance Records",
            font=("Segoe UI", 30, "bold")
        ).pack(pady=20)

    # -----------------------------
    # Reports
    # -----------------------------

    def show_reports(self):

        for widget in self.main.winfo_children():
            widget.destroy()

        ctk.CTkLabel(
            self.main,
            text="Reports",
            font=("Segoe UI", 30, "bold")
        ).pack(pady=20)

    # -----------------------------
    # Clock
    # -----------------------------

    def update_clock(self):

        if hasattr(self, "clock"):

            self.clock.configure(
                text=datetime.now().strftime("%d %B %Y   %I:%M:%S %p")
            )

        self.after(1000, self.update_clock)


if __name__ == "__main__":

    app = Dashboard()
    app.mainloop()