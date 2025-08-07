import qrcode
from PIL import Image

def generar_qr(texto: str, ruta_salida: str) -> None:
    """Generamos un código QR a partir de un texto y lo guardamos en la ruta indicada."""
    # Validamos que el texto no esté vacío
    if not texto.strip():
        raise ValueError("El texto no puede estar vacío")
    
    qr = qrcode.QRCode(
        version=None,  # Auto-ajuste del tamaño
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # Máxima corrección de errores
        box_size=20,   # Píxeles más grandes para mejor contraste
        border=8,      # Borde aún más amplio
    )
    qr.add_data(texto)
    qr.make(fit=True)
    
    # Creamos imagen con máximo contraste negro sobre blanco
    img = qr.make_image(fill_color="#000000", back_color="#FFFFFF").convert('1')  # blanco y negro puro
    # Aumentamos resolución para cámaras de móviles (600x600 mínimo)
    img = img.resize((600, 600), Image.NEAREST)
    # Guardamos con máxima calidad sin compresión y sin perfil de color
    img.save(ruta_salida, format='PNG', optimize=False, compress_level=0, bits=1)
# Generamos códigos QR a partir de texto o URLs
