from master.model.Mesa import Mesa

class MesasMock:
    def __init__(self):
        self.listaMesas = []
        self.listaMesas.append(Mesa(1))
        self.listaMesas.append(Mesa(2))
        self.listaMesas.append(Mesa(3))
        self.listaMesas.append(Mesa(4))
        self.listaMesas.append(Mesa(5))

    def getList(self):
        return self.listaMesas
