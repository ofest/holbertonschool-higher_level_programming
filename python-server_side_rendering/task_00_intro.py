import os

def generate_invitations(template, attendees):
    if not isinstance(template, str) or not isinstance(attendees, list):
        print("Template is not a string or attendees is not a list")
        return

    for value in attendees:
        if not isinstance(value, dict):
            print("Attendees contains a non-dict object")
            return

    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    for idx, attendee in enumerate(attendees, start=1):
        name = attendee.get("name", "N/A") or "N/A"
        event_title = attendee.get("event_title", "N/A") or "N/A"
        event_date = attendee.get("event_date", "N/A") or "N/A"
        event_location = attendee.get("event_location", "N/A") or "N/A"

        output_text = (
            template
            .replace("{name}", name)
            .replace("{event_title}", event_title)
            .replace("{event_date}", event_date)
            .replace("{event_location}", event_location)
        )

        filename = f"output_{idx}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(output_text)
