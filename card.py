import customtkinter as ctk


class DashboardCard(ctk.CTkFrame):
    def __init__(self, parent, title, value, icon="📊"):
        super().__init__(
            parent,
            width=210,
            height=130,
            corner_radius=15
        )

        self.pack_propagate(False)

        self.icon = ctk.CTkLabel(
            self,
            text=icon,
            font=("Segoe UI Emoji", 32)
        )
        self.icon.pack(pady=(15, 5))

        self.value = ctk.CTkLabel(
            self,
            text=str(value),
            font=("Segoe UI", 28, "bold")
        )
        self.value.pack()

        self.title = ctk.CTkLabel(
            self,
            text=title,
            font=("Segoe UI", 14)
        )
        self.title.pack(pady=(5, 10))

    def update_value(self, value):
        self.value.configure(text=str(value))