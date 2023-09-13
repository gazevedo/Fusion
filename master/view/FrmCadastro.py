import customtkinter as ctk

from master.controller.ProdutosController import ProdutosController
from master.controller.ViewController import ViewController
from master.model.Produto import Produto
from master.view.FrmProduto import FrmProduto
from master.view.components.CustomTable import CustomTable

produtosController = ProdutosController()


class FrmCadastro(ctk.CTk, ViewController):

    def __init__(self, root):
        super().__init__()
        self.root = root
        self.setScreenMax()
        self.title("Cadastro de Produtos")
        self._loadView()

    def _loadView(self):
        # frame barra de atalhos
        self.frame_tools = ctk.CTkFrame(self, height=50)
        self.frame_tools.pack(side="top", fill="both")

        self.btn_cadastro = ctk.CTkButton(self.frame_tools, text="Novo", command=lambda: FrmProduto(self.root, self._on_window_close))
        self.btn_cadastro.pack(side="left")

        # Frame Lista
        self.frame_list = ctk.CTkFrame(self)
        self.frame_list.pack(side="left", fill="both", expand=True)

        # criando tabela
        header = ["Código", "Produto", "Descrição", "Valor"]
        self.productTable = CustomTable(self.frame_list, header, produtosController.getListProducts(),
                                        self._on_table_click)
        self.productTable.pack()
        self.mainloop()

    def _on_window_close(self, codigo, nome, descricao, valor):
        # produtosController.listaProdutos.append()
        # self.productTable.insertRow(Produto(codigo, nome, descricao, valor))
        # produto = Produto(codigo, nome, descricao, valor)
        # print(produto.codigo)
        # self.productTable.insertRow()
        print("fechou")
        produto = Produto(codigo, nome, descricao, valor)
        print("cd: " + produto.codigo + "- pr:" + produto.nome + "- desc" + produto.descricao)
        self._loadView()
        self.productTable.insertRow()

    def _on_table_click(self, values):
        FrmProduto(self.root, self.on_window_close, values)
