from master.dal.ProdutosDao import ProdutosDao
from master.model.Produto import Produto
from master.model.Result import Result


class ProdutosController:
    def __init__(self):
        self.produtosDao = ProdutosDao()

    def saveProduct(self, produto):
        result = Result()
        try:
            result.success = self.produtosDao.create(produto)
            if not result.success:
                result.message = "Falha ao salvar produto"

        except Exception as e:
            print("saveProduct:", e)
            result.success = False
            result.message = e
        return result

    def updateProduct(self, produto):
        result = Result()
        try:
            result.success = self.produtosDao.update(produto)
            if not result.success:
                result.message = "Falha ao atualizar produto"
        except Exception as e:
            print("updateProduct:", e)
            result.message = e
        return result

    def deleteProduct(self, produto):
        result = Result()
        try:
            result.success = self.produtosDao.delete(produto)
            if not result.success:
                result.message = "Falha ao deletar produto"
        except Exception as e:
            print("deleteProduct:", e)
            result.message = e
        return result

    def getListProducts(self):
        try:
            list = []
            result = self.produtosDao.getProducts()
            if result is None:
                return []
            else:
                for obj in result:
                    codigo, nome, descricao, valor, imagem = obj
                    new = Produto(codigo, nome, descricao, valor, imagem)
                    list.append(new)
                return list
        except Exception as e:
            print("getListProducts:", e)
            return []
