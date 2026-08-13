import customtkinter as ctk


class RecentActivity(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        title = ctk.CTkLabel(
            self,
            text="Recent Activity",
            font=("Segoe UI", 20, "bold")
        )

        title.pack(anchor="w", padx=15, pady=10)

        self.box = ctk.CTkTextbox(
            self,
            width=650,
            height=280,
            font=("Consolas", 14)
        )

        self.box.pack(padx=15, pady=10)

        self.load_demo()

    def load_demo(self):

        demo = [

            "08:30 AM   Advit Singh           Present",

            "08:32 AM   Aryan Tiwari          Present",

            "08:35 AM   Mandvi               Present",

            "08:41 AM   Unknown Person       Detected",

            "08:45 AM   Akshit Singh         Present",

            "08:52 AM   Agrim Mishra         Present",

            "08:55 AM   Nahid Fatima         Present",

            "09:00 AM   Devesh Agrahari      Present"

        ]

        self.box.delete("1.0", "end")

        for row in demo:
            self.box.insert("end", row + "\n")

    def add_activity(self, text):
        self.box.insert("end", text + "\n")
        self.box.see("end")