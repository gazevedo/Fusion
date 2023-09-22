from master.dal.DbConnection import DbConnection
from master.model.Produto import Produto


class ProdutosController:
    def __init__(self):
        self.DbConnection = DbConnection()
        self.listaProdutos = []
        self.DataBase = "PRODUTOS"

    def SaveProduct(self, produto):
        return self.DbConnection.create(self.DataBase, produto)

    def UpdateProduct(self, produto):
        return self.DbConnection.update(self.DataBase, produto)

    def getListProducts(self):
        result = []
        result = self.DbConnection.getAll(self.DataBase)
        print(result)
        if result is None:
            return []
        return result