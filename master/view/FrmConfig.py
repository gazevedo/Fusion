import customtkinter as ctk

from master.controller.ViewController import ViewController


class FrmConfig(ctk.CTk, ViewController):
    def __init__(self, root):
        super().__init__()