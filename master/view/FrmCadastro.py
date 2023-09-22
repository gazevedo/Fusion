import customtkinter as ctk

from master.controller.ProdutosController import ProdutosController
from master.controller.ViewController import ViewController
from master.model.Produto import Produto
from master.view.FrmProduto import FrmProduto
from master.view.components.CustomTable import CustomTable


class FrmCadastro(ctk.CTk, ViewController):

    def __init__(self, root):
        super().__init__()
        self.setScreenMax()
        self.title("Cadastro de Produtos")
        self.root = root

        self.produtosController = ProdutosController()

        # Frame Barra ferramentas
        self.frame_tools = ctk.CTkFrame(self, height=50)
        self.frame_tools.pack(side="top", fill="both")

        # Frame Lista
        self.frame_list = ctk.CTkFrame(self)
        self.frame_list.pack(side="top", fill="both", expand=True, padx=10, pady=10)

        self.btn_cadastro = ctk.CTkButton(self.frame_tools, text="Novo",
                                          command=lambda: FrmProduto(self.root, self._on_save))
        self.btn_cadastro.pack(side="left")

        # criando tabela
        header = ["Código", "Produto", "Descrição", "Valor"]
        self.productTable = CustomTable(self.frame_list, header, self.produtosController.getListProducts(),
                                        self._on_table_click)

        self.mainloop()

    def _on_save(self, action, index, codigo, nome, descricao, valor):
        newProduct = Produto(codigo, nome, descricao, valor)

        if action == 0:
            result = self.produtosController.SaveProduct(newProduct)
            if result.success:
                self.productTable.insertRow(newProduct)
            else:
                print(result.message)
        elif action == 1:
            result = self.produtosController.UpdateProduct(newProduct)
            if result.success:
                self.productTable.updateRow(newProduct, index)
            else:
                print(result.message)

        else:
            self.productTable.delete(newProduct, index)

    def _on_table_click(self, values, index):
        FrmProduto(self.root, self._on_save, values, index)
