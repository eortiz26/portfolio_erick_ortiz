import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_ticket(pdf_path, ticket_data):
    folder_name = os.path.dirname(pdf_path)
    if folder_name:
        os.makedirs(folder_name, exist_ok=True)

    pdf_canvas = canvas.Canvas(pdf_path, pagesize=letter)
    page_width, page_height = letter

    y_pos = page_height - 50

    pdf_canvas.setFont("Helvetica-Bold", 16)
    pdf_canvas.drawString(50, y_pos, "Demo Traffic Ticket")
    y_pos = y_pos - 30

    pdf_canvas.setFont("Helvetica", 12)
    pdf_canvas.drawString(50, y_pos, "Plate: " + ticket_data["plate_number"])
    y_pos = y_pos - 20

    pdf_canvas.drawString(50, y_pos, "Owner: " + ticket_data["owner_name"])
    y_pos = y_pos - 20

    pdf_canvas.drawString(50, y_pos, "Address: " + ticket_data["mailing_address"])
    y_pos = y_pos - 30

    pdf_canvas.setFont("Helvetica-Bold", 12)
    pdf_canvas.drawString(50, y_pos, "Violations")
    y_pos = y_pos - 20

    pdf_canvas.setFont("Helvetica", 12)
    for item_data in ticket_data["line_items"]:
        row_text = item_data["violation"] + " - $" + str(item_data["price"])
        pdf_canvas.drawString(70, y_pos, row_text)
        y_pos = y_pos - 20

    y_pos = y_pos - 10
    pdf_canvas.setFont("Helvetica-Bold", 12)
    pdf_canvas.drawString(50, y_pos, "Total: $" + str(ticket_data["total"]))
    y_pos = y_pos - 30

    pdf_canvas.setFont("Helvetica-Bold", 12)
    pdf_canvas.drawString(50, y_pos, "Notes")
    y_pos = y_pos - 20

    pdf_canvas.setFont("Helvetica", 11)
    for note_text in ticket_data["notes"]:
        pdf_canvas.drawString(70, y_pos, "- " + note_text)
        y_pos = y_pos - 18

    pdf_canvas.save()