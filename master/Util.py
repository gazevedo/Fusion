import base64

from PIL import Image, ImageTk
import io

from PIL import Image


def convertBase64ToImageTk(strBase64, width=100, heigth=100):
    if strBase64 is None or strBase64 == 'None':
        return ImageTk.PhotoImage(Image.open("Resources/img_sem_imagem.png").resize((width, heigth)))
    else:
        image_bytes = base64.b64decode(strBase64)
        image_pil = Image.open(io.BytesIO(image_bytes)).resize((width, heigth))
        return ImageTk.PhotoImage(image_pil)