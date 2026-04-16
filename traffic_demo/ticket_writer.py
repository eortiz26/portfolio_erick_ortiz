from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def create_ticket(output_path, ticket_data):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    pdf = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter

    y = height - 50

    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(50, y, "Demo Traffic Ticket")
    y -= 30

    pdf.setFont("Helvetica", 11)
    pdf.drawString(50, y, "Plate Number: " + ticket_data["plate_number"])
    y -= 20

    pdf.drawString(50, y, "Owner: " + ticket_data["owner_name"])
    y -= 20

    pdf.drawString(50, y, "Mailing Address: " + ticket_data["mailing_address"])
    y -= 30

    pdf.drawString(50, y, "Violations:")
    y -= 20

    for item in ticket_data["line_items"]:
        line = "- " + item["name"] + ": $" + str(item["price"])
        pdf.drawString(70, y, line)
        y -= 20

    y -= 10
    pdf.drawString(50, y, "Total Fine: $" + str(ticket_data["total"]))
    y -= 30

    pdf.drawString(50, y, "Notes:")
    y -= 20

    for note in ticket_data["notes"]:
        pdf.drawString(70, y, "- " + note)
        y -= 20

    pdf.save()