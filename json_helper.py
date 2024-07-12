import json
import os
from pathlib import Path
import pickle


def read_json(file_path):
    """
    Purpose: 
    """
    # Convert the directory string to a Path object
    file_path = '/Users/teddy/Documents/GitHub/Week3/PythonFundamentals.Exercises.Part9/data/super_smash_bros/link.json'
    json_objects = []

    dir_path = Path(file_path)

    with open(dir_path, 'r') as file:
        json_object = json.load(file)
        return json_object

# end def

def read_all_json_files(directory):
    """
    Reads all JSON files in the specified directory and returns a list of JSON objects.

    :param directory: Path to the directory containing JSON files
    :return: List of JSON objects
    """
    json_objects = []

    # Convert the directory string to a Path object
    dir_path = Path(directory)

    # Iterate over each item in the directory
    for item in dir_path.iterdir():
        # Check if the item is a file and has a .json extension
        if item.is_file() and item.suffix == '.json':
            try:
                # Open and read the JSON file
                with open(item, 'r') as file:
                    json_object = json.load(file)
                    json_objects.append(json_object)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON from file {item.name}: {e}")
            except Exception as e:
                print(f"An error occurred while reading file {item.name}: {e}")

    print(json_objects)



# Call the function and get the list of JSON objects
read_all_json_files('/Users/teddy/Documents/GitHub/Week3/PythonFundamentals.Exercises.Part9/data/super_smash_bros')



#end of def


def write_pickle(pickle_file):
    """
    Reads all JSON files in the specified directory and writes their contents to a pickle file.

    :param directory: Path to the directory containing JSON files
    """
    # Read all JSON objects from the directory
    json_objects = read_all_json_files(directory)

    # Specify the output pickle file

    # Write the JSON objects to the pickle file
    try:
        with open(pickle_file, 'wb') as file:
            pickle.dump(json_objects, file)
        print(f"JSON objects have been written to {pickle_file}")
    except Exception as e:
        print(f"An error occurred while writing to pickle file: {e}")

# Specify the directory (using your example directory)
directory = '/Users/teddy/Documents/GitHub/Week3/PythonFundamentals.Exercises.Part9/data/super_smash_bros'

# Call the function to write JSON objects to a pickle file
write_pickle('super_smash_characters.pickle')

#end of def

def load_pickle(file_path):
    try:
        with open(file_path, 'rb') as file:
            data = pickle.load(file)
            for item in data:
                print(item)
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred while reading the pickle file: {e}")

load_pickle('super_smash_characters.pickle')        
