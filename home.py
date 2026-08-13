import customtkinter as ctk

from gui.card import DashboardCard
from gui.recent_activity import RecentActivity


class HomePage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(2, weight=1)

        # ---------------- Welcome ---------------- #

        welcome = ctk.CTkLabel(
            self,
            text="Welcome, Admin 👋",
            font=("Segoe UI", 28, "bold")
        )

        welcome.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="w",
            padx=20,
            pady=(20, 10)
        )

        # ---------------- Dashboard Cards ---------------- #

        cards = ctk.CTkFrame(self, fg_color="transparent")
        cards.grid(
            row=1,
            column=0,
            columnspan=2,
            padx=20,
            pady=10,
            sticky="ew"
        )

        self.total_card = DashboardCard(
            cards,
            "Total Students",
            256,
            "👨‍🎓"
        )

        self.present_card = DashboardCard(
            cards,
            "Present Today",
            240,
            "✅"
        )

        self.absent_card = DashboardCard(
            cards,
            "Absent Today",
            16,
            "❌"
        )

        self.unknown_card = DashboardCard(
            cards,
            "Unknown Faces",
            2,
            "🚨"
        )

        self.total_card.pack(side="left", padx=10)
        self.present_card.pack(side="left", padx=10)
        self.absent_card.pack(side="left", padx=10)
        self.unknown_card.pack(side="left", padx=10)

        # ---------------- Left Panel ---------------- #

        left = ctk.CTkFrame(self)

        left.grid(
            row=2,
            column=0,
            padx=(20, 10),
            pady=20,
            sticky="nsew"
        )

        left.grid_columnconfigure(0, weight=1)

        quick = ctk.CTkLabel(
            left,
            text="Quick Actions",
            font=("Segoe UI", 20, "bold")
        )

        quick.pack(anchor="w", padx=20, pady=(20, 15))

        actions = [
            "👤 Register Student",
            "📷 Start Attendance",
            "🧠 Train AI Model",
            "📊 Generate Report"
        ]

        for action in actions:
            button = ctk.CTkButton(
                left,
                text=action,
                width=260,
                height=42
            )

            button.pack(pady=10)

        # ---------------- Right Panel ---------------- #

        right = ctk.CTkFrame(self)

        right.grid(
            row=2,
            column=1,
            padx=(10, 20),
            pady=20,
            sticky="nsew"
        )

        activity = RecentActivity(right)
        activity.pack(fill="both", expand=True, padx=10, pady=10)