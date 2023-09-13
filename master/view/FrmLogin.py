import webbrowser

import customtkinter
from master.controller.ViewController import ViewController
from master.view.FrmPrincipal import FrmPrincipal

window_width = 400
window_height = 500
label_width = 300
label_height = 40


class FrmLogin(customtkinter.CTk, ViewController):
    def __init__(self, window):
        super().__init__()
        self.window = window  # Armazena a instância da aplicação
        self.title("LOGIN")
        self.setScreeSize(window_width, window_height)
        self.centerOnScreen(window_width, window_height)

        self.frame_login = customtkinter.CTkFrame(self, corner_radius=10)
        self.frame_login.pack(side="top", fill="both", pady=(80, 0), padx=50)
        # self.overrideredirect(True)  # Oculta a barra de título da janela

        self.login_label = customtkinter.CTkLabel(self.frame_login, text="Bem-Vindo",
                                                  font=customtkinter.CTkFont(size=30, weight="bold"))
        self.login_label.pack(padx=(10, 10), pady=(30, 5))

        self.username_entry = customtkinter.CTkEntry(self.frame_login, width=label_width, placeholder_text="username",
                                                     font=customtkinter.CTkFont(size=16))
        self.username_entry.pack(padx=(10, 10), pady=(30, 10))

        self.password_entry = customtkinter.CTkEntry(self.frame_login, width=label_width, show="*",
                                                     placeholder_text="password", font=customtkinter.CTkFont(size=16))
        self.password_entry.pack(padx=(10, 10))

        self.login_button = customtkinter.CTkButton(self.frame_login, text="Login", width=200,
                                                    command=self.onclick_login)
        self.login_button.pack(padx=(10, 10), pady=(30, 5))

        self.label_link2 = customtkinter.CTkLabel(self.frame_login, text=r"http://www.google.com", cursor="hand2",
                                                  fg_color="transparent")
        self.label_link2.bind("<Button-1>", self.callback)
        self.label_link2.pack(pady=30)

        self.mainloop()

    def onclick_login(self):
        self.destroy()
        FrmPrincipal(self.window)

    def callback(self, event):
        webbrowser.open_new(event.widget.cget("text"))
