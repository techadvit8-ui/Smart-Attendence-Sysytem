import customtkinter as ctk


class Sidebar(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent, width=220, corner_radius=0)

        self.pack_propagate(False)

        title = ctk.CTkLabel(
            self,
            text="SMART\nATTENDANCE",
            font=("Segoe UI", 22, "bold")
        )

        title.pack(pady=(25, 30))

        buttons = [
            "🏠 Home",
            "👤 Register Student",
            "📷 Attendance",
            "📊 Reports",
            "📈 Statistics",
            "⚙ Settings",
            "🚪 Logout"
        ]

        for text in buttons:
            btn = ctk.CTkButton(
                self,
                text=text,
                width=180,
                height=42,
                corner_radius=8
            )
            btn.pack(pady=8)