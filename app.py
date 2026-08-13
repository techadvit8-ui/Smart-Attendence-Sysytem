"""
Smart Attendance System
Main Entry Point
"""

import customtkinter as ctk

# Theme Settings
ctk.set_appearance_mode("dark")      # Modes: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue", "green", "dark-blue"

from gui.splash import SplashScreen

if __name__ == "__main__":
    app = SplashScreen()
    app.mainloop()