#!/usr/bin/env python3

import logging
from string import Template

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def generate_invitations(template, attendees):
 
    # --- Type Validation ---
    if not isinstance(template, str):
        logging.error(f"Invalid input type: template should be a string, got {type(template).__name__}.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        logging.error("Invalid input type: attendees should be a list of dictionaries.")
        return

    # --- Empty Input Checks ---
    if not template.strip():
        logging.error("Template is empty, no output files generated.")
        return

    if not attendees:
        logging.info("No data provided, no output files generated.")
        return

    # --- Process Each Attendee ---
    template_obj = Template(template)

    for idx, attendee in enumerate(attendees, start=1):
        # Replace missing data with 'N/A'
        safe_data = {
            "name": attendee.get("name", "N/A"),
            "event_title": attendee.get("event_title", "N/A"),
            "event_date": attendee.get("event_date", "N/A"),
            "event_location": attendee.get("event_location", "N/A"),
        }

        try:
            # Substitute values into the template
            invitation_text = template_obj.safe_substitute(safe_data)

            # Write to output file
            output_filename = f"output_{idx}.txt"
            with open(output_filename, "w", encoding="utf-8") as file:
                file.write(invitation_text)

            logging.info(f"Generated: {output_filename}")

        except Exception as e:
            logging.error(f"Failed to generate invitation for attendee {idx}: {e}")


# --- Example Usage ---

if __name__ == "__main__":
    template_text = (
        "Dear ${name},\n\n"
        "You are invited to the ${event_title} on ${event_date} "
        "at ${event_location}.\n\n"
        "We look forward to seeing you!\n"
    )

    attendees_list = [
        {"name": "Boba", "event_title": "Vietnam War", "event_date": "March 10, 1974", "event_location": "Hamburger Hill"},
        {"name": "Wallace", "event_title": "Freedom", "event_date": "April 2, 1300", "event_location": "York"},
        {"name": "Alexander", "event_title": "Guagamela", "event_location": "Persia"}
    ]

    generate_invitations(template_text, attendees_list)
