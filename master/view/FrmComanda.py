import random
import tkinter as tk

from master import Util
from master.controller.ProdutosController import ProdutosController
from master.controller.ViewController import ViewController
from master.view.components.CustomTable import CustomTable


class FrmComanda(tk.Toplevel, ViewController):
    def __init__(self):
        super().__init__()
        self.produtosController = ProdutosController()
        self.title("Nova Comanda")
        self.setScreenMax()

        numero_comanda = random.randint(1, 10)

        # paineis
        self.panel_top = tk.Frame(self)
        self.panel_top.pack(side="top", fill="both")

        self.panel_left = tk.Frame(self, bg="white", width=300)
        self.panel_left.pack(side="left", fill="both", pady=20)

        self.panel_right = tk.Frame(self, bg="white")
        self.panel_right.pack(side="left", fill="both", expand=True, padx=10, pady=20)

        # top
        self.panel_top1 = tk.Frame(self.panel_top)
        self.panel_top1.pack(side="top", fill="both")

        self.panel_top2 = tk.Frame(self.panel_top)
        self.panel_top2.pack(side="top", fill="both")

        self.lb_comanda = tk.Label(self.panel_top1, text="Número da comanda:")
        self.lb_comanda.pack(side="left")

        self.lb_numero_comanda = tk.Label(self.panel_top1, text=numero_comanda)
        self.lb_numero_comanda.pack(side="left")

        self.lb_cliente_nome = tk.Label(self.panel_top2, text="Nome:")
        self.lb_cliente_nome.pack(side="left")

        self.lb_cliente_nome = tk.Label(self.panel_top2, text="Joao da Silva")
        self.lb_cliente_nome.pack(side="left")

        # left
        # criando tabela
        header = ["Código", "Descrição", "Unit.", "Qtd.", "Total"]
        self.productTable = CustomTable(self.panel_left, header, 0, 50)

        # right
        self.listProducts = self.produtosController.getListProducts()
        row = 0
        col = 0

        for x in self.listProducts:
            try:
                image = Util.convertBase64ToImageTk(x.imagem, 200, 200)

                # Cria um botão com a imagem e o texto e associa a função de clique
                button = tk.Button(self.panel_right, text=x.nome, image=image, borderwidth=0, highlightthickness=0,
                                   bg="white",
                                   compound="top", bd=0, command=lambda label=x.codigo: self._onclick_item(label))
                button.image = image
                button.grid(row=row, column=col, padx=2, pady=2, sticky="nsew")  # Coloca o botão na linha atual
                # Configurar expansão vertical
                self.panel_right.grid_rowconfigure(row, weight=1)
                # Configurar expansão horizontal
                self.panel_right.grid_columnconfigure(col, weight=1)

                col += 1
                if col > 5:  # Você pode ajustar o número de colunas conforme necessário
                    col = 0
                    row += 1

            except Exception as e:
                print(f"Erro ao carregar a imagem: {e}")

    def _onclick_item(self, id):
        for produto in self.listProducts:
            if produto.codigo == id:
                self.productTable.insertRow(self._convertTableValues(produto))
                break

    def _convertTableValues(self, product):
        # header = ["Código", "Descrição", "Valor", "Qtd.", "Total"]
        return [product.codigo, product.descricao, product.valor, 1, product.valor]