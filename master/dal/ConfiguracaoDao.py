from master.controller.DbController import DbController


class ConfiguracaoDao:
    def __init__(self):
        self.dbController = DbController()

    def getAll(self):
        sql = "SELECT * FROM CONFIGURACAO"
        return self.dbController.executeQuery(sql)

    def addParam(self, chave, valor):
        sql = "INSERT INTO CONFIGURACAO (CHAVE, VALOR) VALUES ('{0}', '{1}') ON CONFLICT (CHAVE) DO UPDATE SET VALOR = '{1}' WHERE CHAVE = '{0}'".format(chave, valor)
        return self.dbController.executeNoQuery(sql)

    def getParam(self, chave):
        sql = "SELECT * FROM CONFIGURACAO WHERE CHAVE = '{0}'".format(chave)
        return self.dbController.executeQuery(sql)