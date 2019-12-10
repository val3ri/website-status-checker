from functions import check_status
import json

# constants: file names
FILE_TO_OPEN = "db.json"
FILE_TO_SAVE_IN = "updated_db.json"

def main():

    # reading our json file and saving it to a variable
    json_file = open(FILE_TO_OPEN, "r")  # Open the JSON file for reading
    json_data = json.load(json_file)  # Read the JSON into the buffer
    json_file.close()  # Close the JSON file

    # magic
    check_status(json_data)

    # Save our changes to JSON file
    json_file = open(FILE_TO_SAVE_IN, "w+")
    json_file.write(json.dumps(json_data))
    json_file.close()


# if __name__ == "__main__":
#     main()
