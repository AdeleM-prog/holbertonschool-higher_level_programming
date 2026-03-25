#!/usr/bin/python3

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Template must be a string")
        return
    if not isinstance(attendees, list):
        print("attendees must be a list")
        return

    if len(template) <= 0:
        print("Template is empty, no output files generated.")
        return
    if attendees == []:
        print("No data provided, no output files generated.")
        return

    for attendee in attendees:
        if not isinstance(attendee, dict):
            print("attendee must be a dict")
            return
        name = attendee.get("name")
        if name is None:
            name = "N/A"

        event_title = attendee.get("event_title")
        if event_title is None:
            event_title = "N/A"
        
        event_date = attendee.get("event_date")
        if event_date is None:
            event_date = "N/A"
        
        event_location = attendee.get("event_location")
        if event_location is None:
            event_location = "N/A"

        