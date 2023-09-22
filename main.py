import customtkinter as ctk

from master.controller.DbController import DbController
from master.view.FrmPrincipal import FrmPrincipal


def main():
    dbcontroller = DbController()
    dbcontroller.executeMigration()

    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")
    app = ctk.CTk()  # Cria uma instância da aplicação
    FrmPrincipal(app)  # Passe a instância da aplicação para a janela de login
    app.mainloop()


if __name__ == "__main__":
    main()
