import cv2
import pytesseract

def extraer_texto_imagen(ruta_imagen: str) -> str:
    """Extraemos texto de una imagen usando OCR."""
    img = cv2.imread(ruta_imagen)
    texto = pytesseract.image_to_string(img)
    return texto
# Extraemos texto de imágenes (OCR)
