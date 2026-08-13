import customtkinter as ctk
from datetime import datetime


class Header(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent, height=70)

        self.pack_propagate(False)

        self.title = ctk.CTkLabel(
            self,
            text="Dashboard",
            font=("Segoe UI", 24, "bold")
        )

        self.title.pack(side="left", padx=20)

        self.time = ctk.CTkLabel(
            self,
            text=""
        )

        self.time.pack(side="right", padx=20)

        self.update_clock()

    def update_clock(self):

        now = datetime.now()

        self.time.configure(
            text=now.strftime("%d %b %Y | %I:%M:%S %p")
        )

        self.after(1000, self.update_clock)