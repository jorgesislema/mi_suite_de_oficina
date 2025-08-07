from PyPDF2 import PdfMerger

def unir_pdfs(lista_rutas, ruta_salida):
    """Unimos varios archivos PDF en uno solo."""
    merger = PdfMerger()
    for ruta in lista_rutas:
        merger.append(ruta)
    merger.write(ruta_salida)
    merger.close()
# Unimos varios archivos PDF en uno solo
