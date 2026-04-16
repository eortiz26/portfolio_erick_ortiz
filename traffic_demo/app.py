import os
from detector import analyze_image
from pricing import calculate_total
from registry import load_registry, lookup_plate
from ticket_writer import create_ticket

def main():
    image_path = "sample_car.jpg"

    analysis = analyze_image(image_path)
    plate_number = analysis["plate_number"]
    violations = analysis["violations"]
    notes = analysis["notes"]

    registry_data = load_registry()
    owner = lookup_plate(plate_number, registry_data)

    if owner is None:
        print("No matching plate found in demo registry.")
        return

    line_items, total = calculate_total(violations)

    ticket_data = {
        "plate_number": plate_number,
        "owner_name": owner["owner_name"],
        "mailing_address": owner["mailing_address"],
        "line_items": line_items,
        "total": total,
        "notes": notes
    }

    output_path = os.path.join("output", "demo_ticket_" + plate_number + ".pdf")
    create_ticket(output_path, ticket_data)

    print("Ticket created at: " + output_path)

if __name__ == "__main__":
    main()