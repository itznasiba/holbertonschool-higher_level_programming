#!/usr/bin/python3
import os

def generate_invitations(template, attendees):
    """
    Generates personalized invitation files from a template and a list of attendees.
    
    :param template: str, the template text containing placeholders.
    :param attendees: list of dicts, data for each attendee.
    """
    # 1. Check Input Types
    if not isinstance(template, str):
        print("Invalid input type: template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Invalid input type: attendees must be a list of dictionaries.")
        return

    # 2. Handle Empty Inputs
    if not template or not template.strip():
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Define the expected placeholders to replace
    placeholders = ["name", "event_title", "event_date", "event_location"]

    # 3. Process Each Attendee
    for index, attendee in enumerate(attendees, start=1):
        personalized_content = template

        for key in placeholders:
            # Safely grab the value. If the key is missing or explicitly None, default to "N/A"
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            
            # Construct the placeholder format used in template.txt (e.g., "{name}")
            placeholder_str = f"{{{key}}}"
            personalized_content = personalized_content.replace(placeholder_str, str(value))

        # 4. Generate Output Files
        filename = f"output_{index}.txt"
        
        try:
            with open(filename, 'w', encoding='utf-8') as output_file:
                output_file.write(personalized_content)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
