
class ViewController:
    def __init__(self):
        super().__init__()
        self.bg_image_label = None
        self.bg_image = None

    def setScreeSize(self, width, height):
        self.geometry(f"{width}x{height}")

    def centerOnScreen(self, width, height):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_position = (screen_width - width) // 2
        y_position = (screen_height - height) // 2
        self.geometry(f"{width}x{height}+{x_position}+{y_position}")

    def setFullScreen(self):
        self.attributes('-fullscreen', True)

    def setScreenMax(self):
        self.after(0, lambda: self.wm_state('zoomed'))
