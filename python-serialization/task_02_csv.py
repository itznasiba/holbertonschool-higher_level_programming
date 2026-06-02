import csv
import json

def convert_csv_to_json(csv_filename):
    """
    Reads data from a CSV file, converts each row into a dictionary,
    and serializes the list of dictionaries into a JSON file named data.json.
    
    :param csv_filename: str, the path to the source CSV file.
    :return: bool, True if conversion succeeded, False if an error occurred.
    """
    try:
        # Open the CSV file for reading
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            # DictReader automatically uses the first row as dictionary keys
            csv_reader = csv.DictReader(csv_file)
            
            # Convert the rows into a standard Python list of dictionaries
            data_list = list(csv_reader)
            
        # Open the target JSON file for writing
        with open('data.json', mode='w', encoding='utf-8') as json_file:
            # Serialize the list of dictionaries to JSON with clean indentation
            json.dump(data_list, json_file, indent=4)
            
        return True

    except FileNotFoundError:
        print(f"Error: The file '{csv_filename}' was not found.")
        return False
    except Exception as e:
        print(f"An unexpected error occurred during conversion: {e}")
        return False
