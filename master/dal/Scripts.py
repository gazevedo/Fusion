class Scripts:
    def __init__(self):
        self.list = []
        self.list.append((0, "CREATE TABLE MIGRATION (Id NUMBER, Date DATE)"))
        self.list.append((1, "CREATE TABLE PRODUTOS (ID NUMBER, NOME TEXT, DESCRICAO TEXT, VALOR NUMBER, IMAGE TEXT)"))
        self.list.append((2, "CREATE TABLE CONFIGURACAO (CHAVE TEXT PRIMARY KEY, VALOR TEXT)"))






        self.list.append((100, "INSERT INTO PRODUTOS (ID , NOME , DESCRICAO , VALOR ) VALUES (1,'produto1','descricao', 20)"))
        self.list.append((101, "INSERT INTO PRODUTOS (ID , NOME , DESCRICAO , VALOR ) VALUES (2,'produto2','descricao', 10)"))
        self.list.append((102, "INSERT INTO PRODUTOS (ID , NOME , DESCRICAO , VALOR ) VALUES (3,'produto3','descricao', 5)"))
        self.list.append((103, "INSERT INTO PRODUTOS (ID , NOME , DESCRICAO , VALOR ) VALUES (4,'produto4','descricao', 7.5)"))
        self.list.append((104, "INSERT INTO PRODUTOS (ID , NOME , DESCRICAO , VALOR ) VALUES (5,'produto5','descricao', 2.30)"))
        self.list.append((105, "INSERT INTO PRODUTOS (ID , NOME , DESCRICAO , VALOR ) VALUES (6,'produto6','descricao', 6)"))

        self.list.append((106, "INSERT INTO CONFIGURACAO (CHAVE, VALOR ) VALUES ('QTD_MESA','10')"))