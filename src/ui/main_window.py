import customtkinter as ctk
from .widgets import (
    WidgetGenerarQR,
    WidgetGenerarBarcode,
    WidgetUnirPDFs,
    WidgetConvertirArchivos,
    WidgetExtraerTextoOCR
)

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Suite de Oficina - Trabajo en Equipo")
        self.geometry("950x650")
        self.resizable(False, False)
        self._crear_pestanas()

    def _crear_pestanas(self):
        self.tabs = ctk.CTkTabview(self)
        self.tabs.pack(fill="both", expand=True, padx=10, pady=10)
        self._agregar_pestana_codigos()
        self._agregar_pestana_documentos()
        self._agregar_pestana_texto()

    def _agregar_pestana_codigos(self):
        tab = self.tabs.add("Códigos")
        ctk.CTkLabel(tab, text="Generamos y leemos códigos QR y de barras para nuestros procesos.", font=("Arial", 14, "bold")).pack(pady=(10, 20))
        WidgetGenerarQR(tab).pack(padx=10, pady=10, fill="x")
        WidgetGenerarBarcode(tab).pack(padx=10, pady=10, fill="x")

    def _agregar_pestana_documentos(self):
        tab = self.tabs.add("Documentos")
        ctk.CTkLabel(tab, text="Cargamos, combinamos y convertimos archivos para optimizar nuestro trabajo.", font=("Arial", 14, "bold")).pack(pady=(10, 20))
        WidgetUnirPDFs(tab).pack(padx=10, pady=10, fill="x")
        WidgetConvertirArchivos(tab).pack(padx=10, pady=10, fill="x")

    def _agregar_pestana_texto(self):
        tab = self.tabs.add("Texto")
        ctk.CTkLabel(tab, text="Extraemos y procesamos texto de imágenes y documentos.", font=("Arial", 14, "bold")).pack(pady=(10, 20))
        WidgetExtraerTextoOCR(tab).pack(padx=10, pady=10, fill="x")


def run_app():
    app = MainWindow()
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")
    app.mainloop()
