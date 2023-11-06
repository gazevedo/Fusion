from tkinter import ttk
import tkinter as tk
import tkinter.font as tkf


class CustomTable(tk.Tk):
    def __init__(self, root, header, colWidth, pad, _on_table_click_callback=None):
        self.root = root
        self._on_table_click_callback = _on_table_click_callback
        self.header = header

        self.tree = ttk.Treeview(self.root, columns=self.header, show="headings")
        self.tree.bind("<Double-1>", self._on_row_click)

        self.scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="right", fill="y")
        self.tree.pack(side="left", fill="both", expand=True)

        for coluna in self.header:
            self.tree.heading(coluna, text=coluna, anchor="w")
            if colWidth == 0 or colWidth is None:
                self.tree.column(coluna, minwidth=0, width=tkf.Font().measure(coluna) + pad)
            else:
                self.tree.column(coluna, width=colWidth, anchor="w")

    def _on_row_click(self, event):
        item = self.tree.selection()[0]
        values = self.tree.item(item, 'values')
        index = self.tree.index(item)
        if self._on_table_click_callback:
            self._on_table_click_callback(values, index)

    def insertRow(self, row):
        self.tree.insert("", "end", values=row)

    def updateRow(self, value, index):
        children = self.tree.get_children()
        if 0 <= index < len(children):
            item = children[index]
            self.tree.item(item, values=value)
        else:
            print(f"Invalid index: {index}")

    def delete(self, index):
        children = self.tree.get_children()
        item = children[index]
        self.tree.delete(item)

    def getIndex(self, col, value):
        for item in self.tree.get_children():
            if self.tree.item(item, "values")[col] == value:
                index = self.tree.index(item)
                return index
            else:
                return -1
