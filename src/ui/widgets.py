from src.modules.text_tools import ocr_tool
import customtkinter as ctk
from tkinter import filedialog, messagebox
from src.modules.code_generators import qr_generator, barcode_generator
from src.modules.file_management import pdf_utils, converter
from src.modules.text_tools import ocr_tool

# ...existing code...

class WidgetExtraerTextoOCR(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.boton_cargar = ctk.CTkButton(self, text="Cargar Imagen", command=self.cargar_imagen)
        self.boton_cargar.pack(pady=5)
        self.texto = ctk.CTkTextbox(self, width=400, height=120)
        self.texto.pack(pady=5)
        self.ruta_imagen = None

    def cargar_imagen(self):
        self.ruta_imagen = filedialog.askopenfilename(filetypes=[("Imágenes", "*.png;*.jpg;*.jpeg;*.bmp")])
        if self.ruta_imagen:
            texto_extraido = ocr_tool.extraer_texto_imagen(self.ruta_imagen)
            self.texto.delete("1.0", "end")
            self.texto.insert("end", texto_extraido)
            messagebox.showinfo("Éxito", "Extraemos el texto de la imagen y lo mostramos.")

import customtkinter as ctk
from tkinter import filedialog, messagebox
from src.modules.code_generators import qr_generator, barcode_generator
from src.modules.file_management import pdf_utils, converter

class WidgetGenerarQR(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.label = ctk.CTkLabel(self, text="Texto para QR:")
        self.label.pack(pady=5)
        self.entrada = ctk.CTkEntry(self, width=300, placeholder_text="Escribimos aquí el texto o URL...")
        self.entrada.pack(pady=5)
        self.boton = ctk.CTkButton(self, text="Generar QR", command=self.generar_qr)
        self.boton.pack(pady=5)
        self.info = ctk.CTkLabel(self, text="Generamos códigos QR optimizados para cámaras móviles", 
                                text_color="gray", font=("Arial", 10))
        self.info.pack(pady=2)

    def generar_qr(self):
        texto = self.entrada.get().strip()
        if not texto:
            messagebox.showwarning("Advertencia", "Escribimos el texto para generar el código QR.")
            return
        
        ruta = filedialog.asksaveasfilename(
            defaultextension=".png", 
            filetypes=[("PNG", "*.png")],
            title="Guardamos el código QR como..."
        )
        if ruta:
            try:
                qr_generator.generar_qr(texto, ruta)
                messagebox.showinfo("Éxito", f"Generamos el código QR y lo guardamos en:\n{ruta}")
            except Exception as e:
                messagebox.showerror("Error", f"No pudimos generar el código QR: {e}")

class WidgetGenerarBarcode(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.label = ctk.CTkLabel(self, text="EAN-13:")
        self.label.pack(pady=5)
        self.entrada = ctk.CTkEntry(self, width=300)
        self.entrada.pack(pady=5)
        self.boton = ctk.CTkButton(self, text="Generar Código de Barras", command=self.generar_barcode)
        self.boton.pack(pady=5)

    def generar_barcode(self):
        ean = self.entrada.get()
        ruta = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG", "*.png")])
        if ean and ruta:
            barcode_generator.generar_barcode(ean, ruta)
            messagebox.showinfo("Éxito", "Generamos el código de barras y lo guardamos.")

class WidgetUnirPDFs(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.boton_cargar = ctk.CTkButton(self, text="Cargar PDFs", command=self.cargar_pdfs)
        self.boton_cargar.pack(pady=5)
        self.boton_unir = ctk.CTkButton(self, text="Unir PDFs", command=self.unir_pdfs)
        self.boton_unir.pack(pady=5)
        self.rutas = []

    def cargar_pdfs(self):
        self.rutas = filedialog.askopenfilenames(filetypes=[("PDF", "*.pdf")])
        if self.rutas:
            messagebox.showinfo("PDFs cargados", f"Cargamos {len(self.rutas)} archivos.")

    def unir_pdfs(self):
        if not self.rutas:
            messagebox.showwarning("Advertencia", "Primero cargamos los archivos PDF.")
            return
        ruta_salida = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF", "*.pdf")])
        if ruta_salida:
            pdf_utils.unir_pdfs(self.rutas, ruta_salida)
            messagebox.showinfo("Éxito", "Combinamos los PDFs en uno solo.")

class WidgetConvertirArchivos(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.boton_csv_excel = ctk.CTkButton(self, text="CSV a Excel", command=self.csv_a_excel)
        self.boton_csv_excel.pack(pady=5)
        self.boton_excel_csv = ctk.CTkButton(self, text="Excel a CSV", command=self.excel_a_csv)
        self.boton_excel_csv.pack(pady=5)
        self.boton_csv_pdf = ctk.CTkButton(self, text="CSV a PDF", command=self.csv_a_pdf)
        self.boton_csv_pdf.pack(pady=5)

    def csv_a_excel(self):
        ruta_csv = filedialog.askopenfilename(filetypes=[("CSV", "*.csv")])
        if not ruta_csv:
            return
        ruta_excel = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel", "*.xlsx")])
        if ruta_excel:
            converter.csv_a_excel(ruta_csv, ruta_excel)
            messagebox.showinfo("Éxito", "Convertimos el CSV a Excel.")

    def excel_a_csv(self):
        ruta_excel = filedialog.askopenfilename(filetypes=[("Excel", "*.xlsx")])
        if not ruta_excel:
            return
        ruta_csv = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV", "*.csv")])
        if ruta_csv:
            converter.excel_a_csv(ruta_excel, ruta_csv)
            messagebox.showinfo("Éxito", "Convertimos el Excel a CSV.")

    def csv_a_pdf(self):
        ruta_csv = filedialog.askopenfilename(filetypes=[("CSV", "*.csv")])
        if not ruta_csv:
            return
        ruta_pdf = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF", "*.pdf")])
        if ruta_pdf:
            converter.csv_a_pdf(ruta_csv, ruta_pdf)
            messagebox.showinfo("Éxito", "Convertimos el CSV a PDF.")
