import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

def csv_a_excel(ruta_csv, ruta_excel):
    """Convertimos un archivo CSV a Excel."""
    df = pd.read_csv(ruta_csv)
    df.to_excel(ruta_excel, index=False)

def excel_a_csv(ruta_excel, ruta_csv):
    """Convertimos un archivo Excel a CSV."""
    df = pd.read_excel(ruta_excel)
    df.to_csv(ruta_csv, index=False)

def csv_a_pdf(ruta_csv, ruta_pdf):
    """Convertimos un archivo CSV a PDF con tabla."""
    df = pd.read_csv(ruta_csv)
    data = [df.columns.tolist()] + df.values.tolist()
    pdf = SimpleDocTemplate(ruta_pdf, pagesize=letter)
    table = Table(data)
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])
    table.setStyle(style)
    elems = [table]
    pdf.build(elems)
# Convertimos entre CSV, Excel y PDF
