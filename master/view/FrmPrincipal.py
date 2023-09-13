import customtkinter as ctk

from master.controller.ProdutosController import ProdutosController
from master.view.FrmCadastro import FrmCadastro
from master.view.components.CustomTable import CustomTable
from master.controller.ViewController import ViewController

produtosController = ProdutosController()


class FrmPrincipal(ctk.CTk, ViewController):
    def __init__(self, root):
        super().__init__()
        self.root = root
        self.setScreenMax()

        # frame barra de atalhos
        self.frame_tools = ctk.CTkFrame(self, height=50)
        self.frame_tools.pack(side="top", fill="both")

        self.btn_cadastro = ctk.CTkButton(self.frame_tools, text="cadastro", command=self.onclick_cadastro)
        self.btn_cadastro.pack(side="left")

        # label
        self.login_label = ctk.CTkLabel(self, text="Texto", font=ctk.CTkFont(size=40, weight="bold"))
        self.login_label.pack(pady=(30, 5))

        # Frame Lista
        self.frame_list = ctk.CTkFrame(self)
        self.frame_list.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        # Frame menu
        self.frame_shortcut = ctk.CTkFrame(self)
        self.frame_shortcut.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        self.search = ctk.CTkEntry(self.frame_shortcut, placeholder_text="pesquisar")
        self.search.pack(side="top", fill="x", padx=10, pady=10)

        # table
        header = ["Produto", "Qtd", "Valor Unit", "Total"]

        self.table = CustomTable(self.frame_list, header, produtosController.listaProdutos)
        self.table.pack()
        self.mainloop()

    def onclick_cadastro(self):
        FrmCadastro(self)
