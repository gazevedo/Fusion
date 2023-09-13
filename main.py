import customtkinter as ctk

from master.view.FrmLogin import FrmLogin
from master.view.FrmPrincipal import FrmPrincipal


def main():
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")
    app = ctk.CTk()  # Cria uma instância da aplicação
    FrmPrincipal(app)  # Passe a instância da aplicação para a janela de login
    app.mainloop()


if __name__ == "__main__":
    main()
