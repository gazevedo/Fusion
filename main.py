import customtkinter as ctk

from View.FrmLogin import FrmLogin
from View.FrmPrincipal import FrmPrincipal


def main():
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")
    app = ctk.CTk()  # Cria uma instância da aplicação
    FrmPrincipal(app)  # Passe a instância da aplicação para a janela de login
    app.mainloop()


if __name__ == "__main__":
    main()
