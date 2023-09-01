import customtkinter as ctk

from Components.CtkTableView import CtkTableView
from Controller.ViewController import ViewController


class FrmPrincipal(ctk.CTk, ViewController):
    def __init__(self, root):
        super().__init__()
        screen_width = self.winfo_screenwidth()

        self.setScreenMax()

        self.frame_tools = ctk.CTkFrame(self, height=50)
        self.frame_tools.pack(side="top", fill="both")

        self.login_label = ctk.CTkLabel(self, text="Texto", font=ctk.CTkFont(size=40, weight="bold"))
        self.login_label.pack(padx=(10, 10), pady=(30, 5))

        # Frame Lista
        self.frame_list = ctk.CTkFrame(self, screen_width / 4 * 3)
        self.frame_list.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        self.table = CtkTableView()
        self.table.setHeaders(["Name", "Age", "Email"])
        self.table.addRow(["John Doe", "25", "johndoe@example.com"])
        self.table.addRow(["Jane Smith", "30", "janesmith@example.com"])

        # Frame menu
        self.frame_shortcut = ctk.CTkFrame(self, screen_width / 4 * 1)
        self.frame_shortcut.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        self.mainloop()

    def onclick_login(self):
        self.destroy()
