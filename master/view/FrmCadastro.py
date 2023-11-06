import tkinter as tk

from master.controller.ProdutosController import ProdutosController
from master.controller.ViewController import ViewController
from master.model.Produto import Produto
from master.view.FrmCadastroItem import FrmCadastroItem
from master.view.components.CustomTable import CustomTable

window_width = 800
window_height = 800


class FrmCadastro(tk.Toplevel, ViewController):

    def __init__(self):
        super().__init__()
        self.centerOnScreen(window_width, window_height)
        self.title("Cadastro de Produtos")

        self.produtosController = ProdutosController()
        self.list_products = self.produtosController.getListProducts()

        # Frame Barra ferramentas
        self.frame_tools = tk.Frame(self, height=50)
        self.frame_tools.pack(side="top", fill="both")

        # Frame Lista
        self.frame_list = tk.Frame(self)
        self.frame_list.pack(side="top", fill="both", expand=True, padx=10, pady=10)

        self.btn_cadastro = tk.Button(self.frame_tools, text="Novo",
                                          command=lambda: FrmCadastroItem(self._on_callback))
        self.btn_cadastro.pack(side="left")

        # criando tabela
        header = ["Código", "Produto", "Descrição", "Valor"]
        self.productTable = CustomTable(self.frame_list, header, 0, 0, self._on_table_click_callback)
        for product in self.list_products:
            self.productTable.insertRow(self._convertTableValues(product))

        self.mainloop()

    def _on_callback(self, action, index, newproduct):
        if action == 0:
            result = self.produtosController.saveProduct(newproduct)
            if result.success:
                self.productTable.insertRow(self._convertTableValues(newproduct))
            else:
                print(result.message)
        elif action == 1:
            result = self.produtosController.updateProduct(newproduct)
            if result.success:
                self.productTable.updateRow(self._convertTableValues(newproduct), index)
            else:
                print(result.message)
        else:
            result = self.produtosController.deleteProduct(newproduct)
            if result.success:
                self.productTable.delete(index)
            else:
                print(result.message)

    def _on_table_click_callback(self, values, index):
        codigo = values[0]
        for produto in self.list_products:
            if str(produto.codigo) == codigo:
                FrmCadastroItem(self._on_callback, produto, index)
                break

    def _convertTableValues(self, product):
        #["Código", "Produto", "Descrição", "Valor"]
        return [product.codigo, product.nome, product.descricao, product.descricao]