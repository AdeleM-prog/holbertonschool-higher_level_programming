#!/usr/bin/python3

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Template must be a string")
        return
    if not isinstance(attendees, list):
        print("attendees must be a list of dictionnaries")
        return

    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        if not isinstance(attendee, dict):
            print("attendee must be a dict")
            return
        invitation = template

        for key in ['name', 'event_title', 'event_date', 'event_location']:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            invitation = invitation.replace(f"{{{key}}}", str(value))
        filename = f"output_{index}.txt"
        with open(filename, "w") as f:
            f.write(invitation)
