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
        #self.productTable.pack()
        # produto = Produto("codigo", "nome", "descricao", 1)
        # self.productTable.insertRow(produto)

        # criando tabela
        header = ["Código", "Produto", "Descrição", "Valor"]
        #product_data = produtosController.getListProducts()
        #self.productTable = CustomTable(self.frame_list, header, product_data, self._on_table_click)
        #self.productTable.pack()
        #self.productTable.insertRow(Produto("codigo", "nome", "descricao", 1))


        self.mainloop()

    def click(self):
        print("click cadastro")
        produto = Produto("123", "nome", "descricao", 1)
        self.productTable.insertRow(produto)

    def _on_save(self, codigo, nome, descricao, valor):
        # produtosController.listaProdutos.append()
        self.productTable.insertRow(Produto(codigo, nome, descricao, valor))
        # produto = Produto(codigo, nome, descricao, valor)
        # print(produto.codigo)
        # self.productTable.insertRow()
        # produto = Produto(codigo, nome, descricao, valor)
        # print("cd: " + produto.codigo + "- pr:" + produto.nome + "- desc" + produto.descricao)
        # self._loadView()
        # self.productTable.insertRow()

    def _on_table_click(self, values):
        FrmProduto(self.root, self._on_save, values)


