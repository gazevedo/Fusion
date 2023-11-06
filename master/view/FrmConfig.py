import tkinter as tk

from master.controller.ConfiguracaoController import ConfiguracaoController
from master.controller.ViewController import ViewController

window_width = 800
window_height = 800

label_width = 50
label_height = 40


class FrmConfig(tk.Tk, ViewController):
    def __init__(self):
        super().__init__()
        self.title("Configurações")
        self.setScreeSize(window_width, window_height)
        self.centerOnScreen(window_width, window_height)

        self.configController = ConfiguracaoController()

        # frame top
        self.frame_top = tk.Frame(self)
        self.frame_top.pack(side="top", fill="both", expand=True, padx=10, pady=10)

        self.lbl_qtd_mesas = tk.Label(self.frame_top, text="Qtd. Mesas:")
        self.lbl_qtd_mesas.pack(side="left")
        self.edt_qtd_mesas = tk.Entry(self.frame_top)
        self.edt_qtd_mesas.pack(side="left")

        # frame bottom
        self.frame_bottom = tk.Frame(self)
        self.frame_bottom.pack(side="top", fill="both", expand=True, padx=10, pady=10)

        self.btn_salvar = tk.Button(self.frame_bottom, text="Salvar", width=50,
                                    command=self._save)
        self.btn_salvar.pack()

        self.lbl_erro = tk.Label(self, fg="red", font=("Roboto", 16))
        self.lbl_erro.pack(side="bottom")

        self._load()

    def _save(self):
        result = self.configController.addParam("qtd_mesa", self.edt_qtd_mesas.get())
        if not result.success:
            self.lbl_erro.config(text=result.message)

    def _load(self):
        dicionario = self.configController.getConfiguracao()
        self.edt_qtd_mesas.insert(tk.END, str(dicionario["qtd_mesa"]))
