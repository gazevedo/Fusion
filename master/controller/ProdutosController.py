from master.dal.ProdutosMock import ProdutosMock
from master.model.Produto import Produto


class ProdutosController:
    def __init__(self):
        self.listaProdutos = ProdutosMock().getList()

    def create(self, codigo, nome, descricao, valor):
        self.listaProdutos.append(Produto(codigo, nome, descricao, valor))

    def read(self, codigo):
        for item in self.listaProdutos:
            if item.codigo == codigo:
                return item
            else:
                return ""

    def update(self, codigo, produto):
        for item in self.listaProdutos:
            if item.codigo == codigo:
                item = produto
                break

    def delete(self, codigo):
        for item in self.listaProdutos:
            if item.codigo == codigo:
                self.listaProdutos.remove(item)
                break

    def getListProducts(self):
        return self.listaProdutos