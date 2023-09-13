import customtkinter as ctk

from Components.CtkTableView import CtkTableView
from Controller.ViewController import ViewController
from master.controller.ProdutosController import ProdutosController
from master.view.components.CustomTable import CustomTable

controller = ProdutosController()


class FrmPrincipal(ctk.CTk, ViewController):

    def __init__(self, root):
        super().__init__()
        self.root = root
        self.screen_width = self.winfo_screenwidth()
        self.setScreenMax()

        self.frame_tools = ctk.CTkFrame(self, height=50)
        self.frame_tools.pack(side="top", fill="both")

        self.label = ctk.CTkLabel(self, text="Texto", font=ctk.CTkFont(size=40, weight="bold"))
        self.label.pack(padx=(10, 10), pady=(30, 5))

        # Frame Lista
        self.frame_list = ctk.CTkFrame(self, self.screen_width / 4 * 3)
        self.frame_list.pack(side="left", fill="both", padx=10, pady=10, expand=True)

        # Frame menu
        self.frame_shortcut = ctk.CTkFrame(self, self.screen_width / 4 * 1)
        self.frame_shortcut.pack(side="right", fill="both", padx=10, pady=10)

        header = ["Código", "Produto", "Descrição", "Valor"]
        self.table = CustomTable(self.frame_list, header, controller.getListProducts())
        self.table.pack(fill="both")




        self.mainloop()

    def onclick_login(self):
        self.destroy()
