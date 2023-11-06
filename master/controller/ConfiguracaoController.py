from master.dal.ConfiguracaoDao import ConfiguracaoDao
from master.model.Result import Result


class ConfiguracaoController:
    def __init__(self):
        super().__init__()
        self.configDao = ConfiguracaoDao()

    def getConfiguracao(self):
        try:
            dicionario = {}
            result = self.configDao.getAll()
            if result is None:
                return []
            else:
                for obj in result:
                    chave, valor = obj
                    dicionario[chave] = valor
                return dicionario
        except Exception as e:
            print("getConfiguracao:", e)
            return []

    def addParam(self, chave, valor):
        result = Result()
        try:
            result.success = self.configDao.addParam(chave, valor)
        except Exception as e:
            result.message = e
            result.success = False
        return result

    def getParam(self, chave):
        try:
            resultSql = self.configDao.getParam(chave)

            if resultSql is not None:
                for obj in resultSql:
                    chave, valor = obj
                    return valor
        except Exception as e:
            print("GerParam erro:", e)

        return None
