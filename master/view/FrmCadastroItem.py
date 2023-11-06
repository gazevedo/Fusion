import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import base64
import io

from master import Util
from master.controller.ViewController import ViewController
from master.model.Produto import Produto

window_width = 400
window_height = 800
label_width = 300
label_height = 40
font_size = 16

ACTION_INSERT = 0
ACTION_UPDATE = 1
ACTION_DELETE = 2


class FrmCadastroItem(tk.Toplevel, ViewController):
    def __init__(self, item_callback=None, _produto="", index=""):
        super().__init__()
        self.produto = _produto
        self.index = index
        self.title("Novo produto")
        self.item_callback = item_callback
        self.setScreeSize(window_width, window_height)
        self.centerOnScreen(window_width, window_height)
        self.image_base64 = None

        # frame
        self.frame_info = tk.Frame(self)
        self.frame_info.pack(side="top", fill="both", expand=True, padx=10, pady=10)

        # codigo
        self.lbl_codigo = tk.Label(self.frame_info, width=label_width, text="Código:", anchor='w')
        self.lbl_codigo.pack(padx=(10, 10), pady=(30, 0))
        self.edtCodigo = tk.Entry(self.frame_info, width=label_width)
        self.edtCodigo.pack(padx=(10, 10), pady=(5, 5))

        # nome
        self.lbl_nome = tk.Label(self.frame_info, width=label_width, text="Nome:", anchor='w')
        self.lbl_nome.pack(padx=(10, 10), pady=(5, 0))
        self.edtNome = tk.Entry(self.frame_info, width=label_width)
        self.edtNome.pack(padx=(10, 10), pady=(5, 5))

        # descricao
        self.lbl_descricao = tk.Label(self.frame_info, width=label_width, text="Descrição:", anchor='w')
        self.lbl_descricao.pack(padx=(10, 10), pady=(5, 0))
        self.edtDescricao = tk.Entry(self.frame_info, width=label_width)
        self.edtDescricao.pack(padx=(10, 10), pady=(5, 5))

        # valor
        self.lbl_valor = tk.Label(self.frame_info, width=label_width, text="Valor:", anchor='w')
        self.lbl_valor.pack(padx=(10, 10), pady=(5, 0))
        self.etValor = tk.Entry(self.frame_info, width=label_width)
        self.etValor.pack(padx=(10, 10), pady=(5, 5))

        #imagem
        self.lb_imagem = tk.Label(self.frame_info )
        self.lb_imagem.pack()

        self.btn_image = tk.Button(self.frame_info, text="Imagem", width=200, command=lambda: self._on_click_image())
        self.btn_image.pack(padx=(10, 10), pady=(50, 5))

        # buttons

        self.btn_salvar = tk.Button(self.frame_info, text="Salvar", width=200, command=lambda: self._on_click_save())
        self.btn_salvar.pack(padx=(10, 10), pady=(50, 5))
        self.btn_delete = tk.Button(self.frame_info, text="Excluir", width=200, command=lambda: self._on_click_delete())
        self.btn_delete.pack(padx=(10, 10), pady=(5, 10))

        self._loadView()
        self.mainloop()

    def _on_click_save(self):
        if self.produto == "":
            action = ACTION_INSERT
        else:
            action = ACTION_UPDATE

        if self.item_callback:
            produto = Produto(self.edtCodigo.get(), self.edtNome.get(), self.edtDescricao.get(), self.etValor.get(),
                              self.image_base64)
            self.item_callback(action, self.index, produto)
        self.destroy()

    def _on_click_delete(self):
        if self.item_callback:
            produto = Produto(self.edtCodigo.get(), self.edtNome.get(), self.edtDescricao.get(), self.etValor.get(),
                              "imagem")
            self.item_callback(ACTION_DELETE, self.index, produto)
        self.destroy()

    def _on_click_image(self):
        caminho_imagem = filedialog.askopenfilename(parent=self,
                                                    filetypes=[("Imagens", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
        # Verifica se o usuário selecionou uma imagem
        if caminho_imagem:
            # Lê a imagem em bytes
            with open(caminho_imagem, "rb") as image_file:
                image_bytes = image_file.read()

            # Converte os bytes da imagem para base64
            self.image_base64 = base64.b64encode(image_bytes).decode('utf-8')
            imagem_tk = Util.convertBase64ToImageTk(self.image_base64)
            self.lb_imagem.config(image=imagem_tk)
            self.lb_imagem.image = imagem_tk
        else:
            print("Nenhuma imagem selecionada.")

    def _loadView(self):
        if not self.produto == "":
            self.edtCodigo.insert(0, self.produto.codigo)
            self.edtNome.insert(0, self.produto.nome)
            self.edtDescricao.insert(0, self.produto.descricao)
            self.etValor.insert(0, self.produto.valor)

            if self.produto.imagem != "" and self.produto.imagem is not None:
                image_tk = Util.convertBase64ToImageTk(self.produto.imagem)
                self.lb_imagem.config(image=image_tk)
                self.lb_imagem.image = image_tk