# import os

# from reportlab.lib.pagesizes import A4
# from reportlab.pdfgen import canvas
# from reportlab.lib import colors

# def export_to_pdf(file, headers, data):
#     c = canvas.Canvas(file, pagesize=A4)
#     width, height = A4

#     logo_path = "logo.png"
#     if os.path.exists(logo_path):
#         c.drawImage(logo_path, 20, height - 60, width=80, preserveAspectRatio=True, mask='auto')

#     c.setFont("Helvetica-Bold", 20)
#     c.drawCentredString(width / 2, height - 50, "BON DE LIVRAISON")

#     c.setFont("Helvetica", 10)
#     x_right = width - 200
#     y_top = height - 50
#     c.drawString(x_right, y_top, "STACI 7")
#     c.drawString(x_right, y_top - 12, "Zone PROLOGIS / Parc de Chanteloup")
#     c.drawString(x_right, y_top - 24, "Bâtiment 1 – 2000 RD n°57")
#     c.drawString(x_right, y_top - 36, "77550 MOISSY-CRAMAYEL")

#     start_y = height - 120
#     row_height = 25
#     col_widths = [120, 200, 50]

#     c.setFillColor(colors.lightgrey)
#     c.rect(20, start_y, sum(col_widths), row_height, fill=True, stroke=False)
#     c.setFillColor(colors.black)
#     c.setFont("Helvetica-Bold", 12)
#     x = 20
#     for i, header in enumerate(headers):
#         c.drawCentredString(x + col_widths[i]/2, start_y + 7, header)
#         x += col_widths[i]

#     y = start_y - row_height
#     c.setFont("Helvetica", 12)
#     for idx, item in enumerate(data):
#         if idx % 2 == 0:
#             c.setFillColorRGB(0.9, 0.95, 1)
#             c.rect(20, y, sum(col_widths), row_height, fill=True, stroke=False)

#         c.setFillColor(colors.black)
#         x = 20
#         for i, val in enumerate(item):
#             c.drawCentredString(x + col_widths[i]/2, y + 7, str(val))
#             x += col_widths[i]

#         y -= row_height
#         if y < 50:
#             c.showPage()
#             y = height - 50

#     c.showPage()
#     c.save()

import os
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet


def export_to_pdf(file, context):
    doc = SimpleDocTemplate(file, pagesize=A4)
    story = []
    styles = getSampleStyleSheet()

    # Logo
    logo_path = context.get("logo_path")
    if os.path.exists(logo_path):
        img = Image(logo_path, width=80, height=40, hAlign='LEFT')  # ajuste les dimensions
        story.append(img)

    # Titre centré
    story.append(Spacer(1, 12))
    story.append(Paragraph(f"<para align='center'><b><font size=18>{context.get("title")}</font></b></para>", styles["Normal"]))
    story.append(Spacer(1, 20))

    def format_address(name, address_1, address_2, zip, city):
        # Adresse alignée à droite
        return f"""<para align='right'>
            {name}<br/>
            {address_1}<br/>
            {address_2}<br/>
            {zip} {city}
        </para>
        """
    story.append(Paragraph(format_address(**context.get("contact")), styles["Normal"]))
    story.append(Spacer(1, 30))

    # Table (headers + data)
    col_widths = [250, 250, 50]
    table_data = context.get('table_data')
    table = Table(table_data, colWidths=col_widths)

    # Styles de la table
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),  # header
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.grey),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
    ]))

    # Alternance couleur lignes
    for row_idx in range(1, len(table_data)):
        if row_idx % 2 == 0:
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, row_idx), (-1, row_idx), colors.Color(0.9, 0.95, 1))
            ]))

    story.append(table)

    # Build PDF
    doc.build(story)
