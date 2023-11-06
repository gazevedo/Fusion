import tkinter as tk
from PIL import Image, ImageTk

from master.controller.ViewController import ViewController
from master.view.FrmComanda import FrmComanda
from master.view.FrmCadastro import FrmCadastro
from master.view.FrmConfig import FrmConfig

ACAO_NOVA_COMANDA = 1
ACAO_CADASTRO_PRODUTO = 2
ACAO_CONFIGURACAO = 3
ACAO_CONTROLE_MESA = 4
ACAO_CONTROLE_COMANDA = 5

img_button_size = 100

class FrmPrincipal(tk.Tk, ViewController):
    def __init__(self):
        super().__init__()
        self.setScreenMax()
        self.title("Sistema")

        # var
        img_comanda = ImageTk.PhotoImage(Image.open("Resources/img_comanda.png").resize((img_button_size, img_button_size)))
        img_cadastro_produto = ImageTk.PhotoImage(Image.open("Resources/img_cardapio.png").resize((img_button_size, img_button_size)))
        img_configuracao = ImageTk.PhotoImage(Image.open("Resources/img_configuracao.png").resize((img_button_size, img_button_size)))
        self.formulario_atual = None

        # # frames
        self.panel = tk.Frame(self)
        self.panel.pack(padx=100, pady=100)

        # botoes
        self.btn_comanda = tk.Button(self.panel, text="Comanda", image=img_comanda, command=lambda: self._onclick_menu(ACAO_NOVA_COMANDA))
        self.btn_comanda.pack(side="left", padx=20)


        self.btn_cadastro = tk.Button(self.panel, text="Prod.", image=img_cadastro_produto, command=lambda: self._onclick_menu(ACAO_CADASTRO_PRODUTO))
        self.btn_cadastro.pack(side="left", padx=20)

        self.btn_config = tk.Button(self.panel, text="Config.", image=img_configuracao, command=lambda: self._onclick_menu(ACAO_CONFIGURACAO))
        self.btn_config.pack(side="left", padx=20)
        self.mainloop()

    def _onclick_menu(self, id):
        if id == ACAO_NOVA_COMANDA:
            FrmComanda()
        elif id == ACAO_CADASTRO_PRODUTO:
            FrmCadastro()
        elif id == ACAO_CONFIGURACAO:
            FrmConfig()