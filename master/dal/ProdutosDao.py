from master.controller.DbController import DbController


class ProdutosDao:
    def __init__(self):
        self.dbController = DbController()

    def create(self, produto):
        sql = "insert into produtos(id, nome, descricao, valor, imagem) values ({0}, '{1}', '{2}', {3}, '{4}')".format(
            produto.codigo, produto.nome, produto.descricao, produto.valor, produto.imagem)
        return self.dbController.executeNoQuery(sql)

    def update(self, produto):
        sql = "update produtos set nome='{1}', descricao='{2}', valor={3}, imagem='{4}' where id = {0}".format(
            produto.codigo, produto.nome, produto.descricao, produto.valor, produto.imagem)
        return self.dbController.executeNoQuery(sql)

    def delete(self, produto):
        sql = "delete from produtos where id = {0}".format(produto.codigo)
        return self.dbController.executeNoQuery(sql)

    def getProducts(self):
        sql = "select * from produtos"
        return self.dbController.executeQuery(sql)

