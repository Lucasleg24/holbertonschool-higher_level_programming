import os

def generate_invitations(template, attendees):

  if not isinstance(template, str):
    print("Template is not a string")
    return

  if not isinstance(attendees, list) or not all (
            isinstance(item, dict) for item in attendees):
    print("Attendees is not a list of dictionaries")
    return

  if not template:
        print("Template is empty, no output files generated.")
        return

  if not attendees:
        print("No data provided, no output files generated.")
        return