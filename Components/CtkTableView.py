import customtkinter as ctk
import tkinter as tk


class CtkTableView(ctk.CTk):
    header = []
    data = []

    def __init__(self, root):
        self.root = root
        self.label = "" #teste

        widths = [100, 50, 200]
        for row, row_data in enumerate(self.data, start=1):
            for col, value in enumerate(row_data):
                self.entry = ctk.CTkEntry(self.root, width=widths[col])
                self.entry.insert(tk.END, value)
                self.entry.grid(row=row, column=col, padx=10, pady=5)

    def get_table_data(self):
        table_data = []
        for row in range(1, len(self.data) + 1):
            row_data = []
            for col in range(len(self.headers)):
                self.entry = self.root.grid_slaves(row=row, column=col)[0]
                row_data.append(self.entry.get())
            table_data.append(row_data)
        return table_data

    def setHeaders(self, obj):
        self.header = obj
        for col, header in enumerate(self.headers):
            self.label = tk.Label(self.root, text=header, font=("Arial", 12, "bold"))
            self.label.grid(row=0, column=col, padx=10, pady=5)

    def addRow(self, obj):
        self.header = obj