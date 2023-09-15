from tkinter import ttk

import customtkinter as ctk


class CustomTable(ctk.CTk):

    def __init__(self, root, header, data, onclick=None):
        self.root = root
        self.onclick = onclick
        self.header = header
        self.data = data
        self.tree = ttk.Treeview(self.root, columns=self.header, show="headings")
        self.tree.bind("<Double-1>", self._on_row_click)

        for coluna in self.header:
            self.tree.heading(coluna, text=coluna, anchor="w")
            self.tree.column(coluna, anchor="w")

        for produto in self.data:
            self.tree.insert("", "end", values=(produto.codigo, produto.nome, produto.descricao, produto.valor))

        self.scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="right", fill="y")
        self.tree["height"] = 5
        self.tree.pack(side="left", fill="both", expand=True)

    def _on_row_click(self, event):
        item = self.tree.selection()[0]  # Pega o item selecionado na Treeview
        values = self.tree.item(item, 'values')  # Pega os valores da linha selecionada
        if self.onclick:
            self.onclick(values)

    def insertRow(self, row):
        print("inere linha")
        self.tree.insert("", "end", values=(row.codigo, row.nome, row.descricao, row.valor))
