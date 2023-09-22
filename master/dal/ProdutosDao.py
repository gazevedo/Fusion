from master.model.Produto import Produto


class ProdutosDao:
    def __init__(self):
        self.listaProdutos = []
        self.listaProdutos.append(Produto(1, "Produto1", "desc1", 5))
        self.listaProdutos.append(Produto(2, "Produto2", "desc2", 7.10))
        self.listaProdutos.append(Produto(3, "Produto3", "desc3", 2.50))
        self.listaProdutos.append(Produto(4, "Produto4", "desc4", 18.70))
        self.listaProdutos.append(Produto(5, "Produto5", "desc5", 54.20, ))

    def getList(self):
        return self.listaProdutos
