import barcode
from barcode.writer import ImageWriter

def generar_barcode(ean: str, ruta_salida: str) -> None:
    """Generamos un código de barras EAN-13 y lo guardamos en la ruta indicada."""
    ean13 = barcode.get('ean13', ean, writer=ImageWriter())
    ean13.save(ruta_salida)
# Generamos códigos de barras EAN-13
