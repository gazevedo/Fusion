import customtkinter as ctk

from master.controller.ViewController import ViewController
from master.view.Formulario2 import Formulario2
from master.view.FrmCadastro import FrmCadastro
from master.view.FrmConfig import FrmConfig
from master.view.FrmControleMesa import FrmControleMesa

FRM_CADASTRO = 1
FRM_CONFIG = 2

FRM_CTRL_MESA = 3
FRM_CTRL_COMANDA = 4

class FrmPrincipal(ctk.CTk, ViewController):
    def __init__(self, root):
        super().__init__()
        self.root = root
        self.setScreenMax()
        self.title("Sistema")

        # frame menu ferramentas
        self.frame_tools = ctk.CTkFrame(self, height=50)
        self.frame_tools.pack(side="top", fill="both")

        # frame menu views
        self.frame_views = ctk.CTkFrame(self, width=50, corner_radius=0)
        self.frame_views.pack(side="left", fill="both")

        #botoes
        self.btn_cadastro = ctk.CTkButton(self.frame_tools, text="Prod.", width=50, height=50, command=lambda: self._onclick_menu(FRM_CADASTRO))
        self.btn_cadastro.pack(side="left")
        self.btn_config = ctk.CTkButton(self.frame_tools, text="Config.", width=50, height=50, command=lambda: self._onclick_menu(FRM_CONFIG))
        self.btn_config.pack(side="left")

        self.botao_formulario1 = ctk.CTkButton(self.frame_views, text="Fr1", width=50, command=lambda: self._onclick_view(FRM_CTRL_MESA))
        self.botao_formulario1.pack(pady=(200, 3))

        self.botao_formulario2 = ctk.CTkButton(self.frame_views, text="Fr2", width=50, command=lambda: self._onclick_view(FRM_CTRL_COMANDA))
        self.botao_formulario2.pack()

        self.formulario_atual = None  # Para controlar o formulário exibido

        self.mainloop()

    def _onclick_menu(self, id):
        if id == FRM_CADASTRO:
            FrmCadastro(self)
        elif id == FRM_CONFIG:
            FrmConfig(self)

    def _onclick_view(self, id):
        newForm = None
        if self.formulario_atual:
            self.formulario_atual.destroy()

        if id == FRM_CTRL_MESA:
            newForm = FrmControleMesa(self)
        elif id == FRM_CTRL_COMANDA:
            newForm = Formulario2(self)

        self.formulario_atual = newForm
        newForm.pack(side="left", fill="both", expand=True)