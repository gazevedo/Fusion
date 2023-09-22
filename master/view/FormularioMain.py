import tkinter as tk

from master.view.FrmControleMesa import Formulario1
from master.view.Formulario2 import Formulario2


class FormularioMain(tk.Tk):
    def __init__(self, root):
        super().__init__()
        self.title("Formulário Main")

        self.formulario_atual = None  # Para controlar o formulário exibido

        self.botao_formulario1 = tk.Button(self, text="Abrir Formulário 1", command=self.abrir_formulario1)
        self.botao_formulario1.pack(pady=10)

        self.botao_formulario2 = tk.Button(self, text="Abrir Formulário 2", command=self.abrir_formulario2)
        self.botao_formulario2.pack(pady=10)
        self.mainloop()

    def abrir_formulario1(self):
        # Fecha o formulário atual, se existir
        if self.formulario_atual:
            self.formulario_atual.destroy()

        # Cria o Formulário 1 e o exibe
        formulario1 = Formulario1(self)
        self.formulario_atual = formulario1
        formulario1.pack()

    def abrir_formulario2(self):
        # Fecha o formulário atual, se existir
        if self.formulario_atual:
            self.formulario_atual.destroy()

        # Cria o Formulário 2 e o exibe
        formulario2 = Formulario2(self)
        self.formulario_atual = formulario2
        formulario2.pack()
