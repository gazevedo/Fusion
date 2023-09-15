import customtkinter as ctk

from master.controller.ViewController import ViewController
from master.controller.ProdutosController import ProdutosController
from master.model.Produto import Produto
from master.view.FrmProduto import FrmProduto
from master.view.components.CustomTable import CustomTable

produtosController = ProdutosController()


class FrmCadastro(ctk.CTk, ViewController):

    def __init__(self, root):
        super().__init__()
        self.setScreenMax()
        self.title("Cadastro de Produtos")
        self.root = root

        # Frame Barra
        self.frame_tools = ctk.CTkFrame(self, height=50)
        self.frame_tools.pack(side="top", fill="both")

        # Frame Lista
        self.frame_list = ctk.CTkFrame(self)
        self.frame_list.pack(side="top", fill="both", expand=True, padx=10, pady=10)

        self.btn_cadastro = ctk.CTkButton(self.frame_tools, text="Novo", command=lambda: FrmProduto(self.root, self._on_save))
        self.btn_cadastro.pack(side="left")

        # self.btn_teste = ctk.CTkButton(self.frame_tools, text="btn_teste", command=self.click)
        # self.btn_teste.pack(side="left")

        # criando tabela
        header = ["Código", "Produto", "Descrição", "Valor"]
        self.productTable = CustomTable(self.frame_list, header, produtosController.getListProducts(), self._on_table_click)

        # criando tabela
        header = ["Código", "Produto", "Descrição", "Valor"]
        self.mainloop()

    def _on_save(self, codigo, nome, descricao, valor, index):
        if (index == ""):
            self.productTable.insertRow(Produto(codigo, nome, descricao, valor))
        else:
            print("edit")
            self.productTable.updateRow(Produto(codigo, nome, descricao, valor), index)

    def _on_table_click(self, values, index):
        FrmProduto(self.root, self._on_save, values, index)


