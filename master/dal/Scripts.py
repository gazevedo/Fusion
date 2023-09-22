class Scripts:
    def __init__(self):
        self.list = []
        self.list.append((0, "CREATE TABLE MIGRATION (Id NUMBER, Date DATE)"))
        self.list.append((1, "CREATE TABLE PRODUTOS (ID NUMBER, NOME TEXT, DESCRICAO, TEXT, VALOR NUMBER)"))