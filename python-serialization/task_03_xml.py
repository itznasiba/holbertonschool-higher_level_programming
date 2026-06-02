import xml.etree.ElementTree as ET
import os

def serialize_to_xml(dictionary, filename):
    """
    Serializes a flat Python dictionary into an XML file.
    
    :param dictionary: dict, the data to serialize.
    :param filename: str, the destination XML file path.
    """
    # Create the root element <data>
    root = ET.Element("data")
    
    # Iterate through the dictionary and add items as child elements
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        # XML tags require string text content
        child.text = str(value)
        
    # Wrap the root in an ElementTree object
    tree = ET.ElementTree(root)
    
    try:
        # Write the tree to the specified file
        # xml_declaration adds <?xml version='1.0' encoding='utf-8'?> (optional, but standard)
        tree.write(filename, encoding="utf-8", xml_declaration=True)
        return True
    except Exception as e:
        print(f"Error writing XML to {filename}: {e}")
        return False


def deserialize_from_xml(filename):
    """
    Reads an XML file and parses it back into a flat Python dictionary.
    
    :param filename: str, the source XML file path.
    :return: dict, the reconstructed dictionary, or None if an error occurs.
    """
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' does not exist.")
        return None

    try:
        # Parse the XML file into an ElementTree object
        tree = ET.parse(filename)
        root = tree.getroot()
        
        # Reconstruct the dictionary from the child elements
        reconstructed_dict = {}
        for child in root:
            reconstructed_dict[child.tag] = child.text
            
        return reconstructed_dict
        
    except ET.ParseError as e:
        print(f"Error parsing XML file {filename}: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred during deserialization: {e}")
        return None
