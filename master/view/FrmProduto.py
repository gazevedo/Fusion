import customtkinter as ctk

from master.controller.ViewController import ViewController
from master.controller.ProdutosController import ProdutosController

window_width = 400
window_height = 500
label_width = 300
label_height = 40
font_size = 16


class FrmProduto(ctk.CTk, ViewController):
    def __init__(self, root, save_callback=None, object="", index=""):
        super().__init__()
        self.produtoController = ProdutosController()
        self.root = root
        self.object = object
        self.index = index
        self.title("Novo produto")
        self.save_callback = save_callback
        #self.protocol("WM_DELETE_WINDOW", self._on_window_close)
        self.setScreeSize(window_width, window_height)
        self.centerOnScreen(window_width, window_height)

        self.frame_info = ctk.CTkFrame(self)
        self.frame_info.pack(side="top", fill="both", expand=True, padx=10, pady=10)

        self.lbl_codigo = ctk.CTkLabel(self.frame_info, width=label_width, text="Código:", font=ctk.CTkFont(size=font_size), anchor='w')
        self.lbl_codigo.pack( padx=(10, 10), pady=(30, 0))
        self.etCodigo = ctk.CTkEntry(self.frame_info, width=label_width, font=ctk.CTkFont(size=font_size))
        self.etCodigo.pack(padx=(10, 10), pady=(5, 5))

        self.lbl_nome = ctk.CTkLabel(self.frame_info, width=label_width, text="Nome:", font=ctk.CTkFont(size=font_size), anchor='w')
        self.lbl_nome.pack(padx=(10, 10), pady=(5, 0))
        self.etNome = ctk.CTkEntry(self.frame_info, width=label_width, font=ctk.CTkFont(size=font_size))
        self.etNome.pack(padx=(10, 10), pady=(5, 5))

        self.lbl_descricao = ctk.CTkLabel(self.frame_info, width=label_width, text="Descrição:", font=ctk.CTkFont(size=font_size), anchor='w')
        self.lbl_descricao.pack(padx=(10, 10), pady=(5, 0))
        self.etDescricao = ctk.CTkEntry(self.frame_info, width=label_width, font=ctk.CTkFont(size=font_size))
        self.etDescricao.pack(padx=(10, 10), pady=(5, 5))

        self.lbl_valor = ctk.CTkLabel(self.frame_info, width=label_width, text="Valor:", font=ctk.CTkFont(size=font_size), anchor='w')
        self.lbl_valor.pack(padx=(10, 10), pady=(5, 0))
        self.etValor = ctk.CTkEntry(self.frame_info, width=label_width, font=ctk.CTkFont(size=font_size))
        self.etValor.pack(padx=(10, 10), pady=(5, 5))

        self.btn_salvar = ctk.CTkButton(self.frame_info, text="Salvar", width=200, command=self._on_click_salvar)
        self.btn_salvar.pack(padx=(10, 10), pady=(50, 10))
        if self.object == "":
            pass
        else:
            self._loadView()
            self.edit = True

        self.mainloop()

    def _on_click_salvar(self):
        if self.save_callback:
            self.save_callback(self.etCodigo.get(), self.etNome.get(), self.etDescricao.get(), self.etValor.get(), self.index)
        self.destroy()

    def _loadView(self):
        self.etCodigo.insert(0, self.object[0])
        self.etNome.insert(0, self.object[1])
        self.etDescricao.insert(0, self.object[2])
        self.etValor.insert(0, self.object[3])

