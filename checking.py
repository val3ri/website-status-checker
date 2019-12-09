from functions import check_status
import json


def main():

    # with open('db.json', 'r+') as db:
    #     json_data = db.read()
    # data = json.loads(json_data)
    # check_status(data)

    # data = open('db.json', 'r+')
    # json_data = json.loads(data.read())
    # check_status(json_data)

    # stackoverflow code
    json_file = open("db.json", "r")  # Open the JSON file for reading
    json_data = json.load(json_file)  # Read the JSON into the buffer
    json_file.close()  # Close the JSON file

    # Working with buffered content
    # tmp = data["location"]
    # data["location"] = path
    # data["mode"] = "replay"

    # magic
    check_status(json_data)
    print(json_data)
    # /magic

    # Save our changes to JSON file
    json_file = open("updated_db.json", "w+")
    json_file.write(json.dumps(json_data))
    json_file.close()
    # stackoverflow code

    print(json_data)


if __name__ == "__main__":
    main()


# def update_json_file():
#     json_file = open("replayScript.json", "r") # Open the JSON file for reading
#     data = json.load(json_file) # Read the JSON into the buffer
#     json_file.close() # Close the JSON file

#     ## Working with buffered content
#     tmp = data["location"]
#     data["location"] = path
#     data["mode"] = "replay"

#     ## Save our changes to JSON file
#     json_file = open("replayScript.json", "w+")
#     json_file.write(json.dumps(data))
#     json_file.close()
