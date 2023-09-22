import customtkinter as ctk

class VendaBalcao(ctk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.config(bg="lightblue")

        label = tk.Label(self, text="Este é o Formulário 1", font=("Arial", 14))
        label.pack(padx=20, pady=20)