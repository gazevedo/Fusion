import customtkinter as ctk


class FrmControleMesa(ctk.CTkFrame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.configure(corner_radius=0, fg_color='white')

        label = ctk.CTkLabel(self, text="Este é o Formulário 1", font=("Arial", 14))
        label.pack(padx=20, pady=20)