import os
import streamlit as st
from detector import analyze_image
from pricing import make_line_items
from registry import load_registry, lookup_plate
from ticket_writer import create_ticket

st.set_page_config(page_title="Demo Ticket Review", layout="wide")

st.title("Demo Ticket Review App")
st.write("This is a safe practice project. A human must review before a ticket is created.")

default_image_path = "images/sample_car.jpg"

st.subheader("Step 1: Pick an image")
image_path = st.text_input("Image path", value=default_image_path)

if os.path.exists(image_path):
    st.image(image_path, caption="Review Image", use_container_width=True)
else:
    st.warning("Image file not found. Put a test image at images/sample_car.jpg")

if st.button("Analyze Image"):
    try:
        analysis_data = analyze_image(image_path)
        st.session_state["analysis_data"] = analysis_data
    except Exception as error_obj:
        st.error(str(error_obj))

if "analysis_data" in st.session_state:
    analysis_data = st.session_state["analysis_data"]

    st.subheader("Step 2: Human Review")

    detected_plate = analysis_data["plate_number"]
    detected_violations = analysis_data["violations"]
    detected_notes = analysis_data["notes"]

    st.write("### Suggested plate")
    edited_plate = st.text_input("Plate number", value=detected_plate)

    st.write("### Suggested violations")

    broken_light_val = st.checkbox(
        "broken_light",
        value="broken_light" in detected_violations
    )
    expired_tag_val = st.checkbox(
        "expired_tag",
        value="expired_tag" in detected_violations
    )
    speeding_val = st.checkbox(
        "speeding",
        value="speeding" in detected_violations
    )
    red_light_val = st.checkbox(
        "red_light",
        value="red_light" in detected_violations
    )

    approved_violations = []

    if broken_light_val:
        approved_violations.append("broken_light")
    if expired_tag_val:
        approved_violations.append("expired_tag")
    if speeding_val:
        approved_violations.append("speeding")
    if red_light_val:
        approved_violations.append("red_light")

    st.write("### Detector notes")
    for note_text in detected_notes:
        st.write("- " + note_text)

    registry_data = load_registry()
    owner_data = lookup_plate(edited_plate, registry_data)

    if owner_data is None:
        st.error("No matching demo plate found in registry.")
    else:
        st.write("### Matched demo registry record")
        st.write("Owner: " + owner_data["owner_name"])
        st.write("Address: " + owner_data["mailing_address"])

        line_items, total_amount = make_line_items(approved_violations)

        st.write("### Ticket preview")
        for item_data in line_items:
            st.write(item_data["violation"] + " -> $" + str(item_data["price"]))
        st.write("**Total: $" + str(total_amount) + "**")

        reviewer_name = st.text_input("Reviewer name", value="Human Reviewer")

        if st.button("Approve Ticket and Create PDF"):
            ticket_data = {
                "plate_number": edited_plate,
                "owner_name": owner_data["owner_name"],
                "mailing_address": owner_data["mailing_address"],
                "line_items": line_items,
                "total": total_amount,
                "notes": detected_notes + ["Approved by: " + reviewer_name]
            }

            output_path = os.path.join("output", "demo_ticket_" + edited_plate + ".pdf")
            create_ticket(output_path, ticket_data)

            st.success("Ticket created successfully")
            st.write("Saved file: " + output_path)