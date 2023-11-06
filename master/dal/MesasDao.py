from master.controller.DbController import DbController


class MesasDao:
    def __init__(self):
        self.dbController = DbController()

    def create(self, chave, valor):
        sql = "INSERT INTO CONFIGURACAO(CHAVE, VALOR) values ({0}, {1})".format(chave, valor)
        return self.dbController.executeNoQuery(sql)

    # def update(self, produto):
    #     sql = "update produtos set nome = '{1}', descricao = '{2}', valor = {3} where id = {0}".format(produto.codigo, produto.nome, produto.descricao, produto.valor)
    #     return self.dbController.executeNoQuery(sql)
    #
    # def delete(self, produto):
    #     sql = "delete from produtos where id = {0}".format(produto.codigo)
    #     return self.dbController.executeNoQuery(sql)
    #
    # def getProducts(self):
    #     sql = "select * from produtos"
    #     return self.dbController.executeQuery(sql)

