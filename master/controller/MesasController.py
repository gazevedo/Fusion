from master.dal.MesasMock import MesasMock
from master.model.Mesa import Mesa


class MesasController:
    def __init__(self):
        self.listaMesas = MesasMock().getList()

    def create(self, id):
        self.listaMesas.append(Mesa(id))

    def read(self, id):
        for item in self.listaMesas:
            if item.id == id:
                return item
            else:
                return ""

    def delete(self, id):
        for item in self.listaMesas:
            if item.id == id:
                self.listaMesas.remove(item)
                break

    def getListMesas(self):
        return self.listaMesas