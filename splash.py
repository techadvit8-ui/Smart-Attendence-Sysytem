import customtkinter as ctk


class SplashScreen(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Smart Attendance System")
        self.geometry("700x450")
        self.resizable(False, False)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.configure(fg_color="#1E1E1E")

        # Center Window
        self.center_window()

        # Title
        self.title_label = ctk.CTkLabel(
            self,
            text="Smart Attendance System",
            font=("Segoe UI", 30, "bold")
        )
        self.title_label.pack(pady=(80, 10))

        # Subtitle
        self.subtitle = ctk.CTkLabel(
            self,
            text="AI Powered Face Recognition",
            font=("Segoe UI", 18)
        )
        self.subtitle.pack()

        # Status Label
        self.status = ctk.CTkLabel(
            self,
            text="Initializing...",
            font=("Segoe UI", 14)
        )
        self.status.pack(pady=(50, 10))

        # Progress Bar
        self.progress = ctk.CTkProgressBar(
            self,
            width=500,
            height=18
        )

        self.progress.pack()
        self.progress.set(0)

        # Version
        self.version = ctk.CTkLabel(
            self,
            text="Version 1.0",
            font=("Segoe UI", 12)
        )

        self.version.pack(side="bottom", pady=20)

        self.value = 0

        self.after(100, self.loading)

    def loading(self):

        self.value += 0.01
        self.progress.set(self.value)

        if self.value < 0.30:
            self.status.configure(text="Loading Modules...")

        elif self.value < 0.60:
            self.status.configure(text="Connecting Database...")

        elif self.value < 0.90:
            self.status.configure(text="Preparing AI Engine...")

        elif self.value < 1.0:
            self.status.configure(text="Launching Application...")

        if self.value < 1:
            self.after(30, self.loading)

        else:
            self.status.configure(text="Done!")
            self.after(800, self.finish)

    def finish(self):
         self.destroy()

         from gui.login import LoginWindow

         login = LoginWindow()
         login.mainloop()
        

    def center_window(self):

        width = 700
        height = 450

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))

        self.geometry(f"{width}x{height}+{x}+{y}")


if __name__ == "__main__":
    app = SplashScreen()
    app.mainloop()