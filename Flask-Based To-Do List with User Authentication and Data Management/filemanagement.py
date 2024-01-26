import os
import json

def create_file(username):
    directory = "userfile"
    file_path = os.path.join(directory, username + ".json")

    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(file_path, "w") as file:
        file.write('{"tasks":[]}')
        pass


def read_json_file(username):
    directory = "userfile"
    file_path = os.path.join(directory, username + ".json")

    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            data = json.load(file)
            return data
    else:
        print(f"File {file_path} does not exist.")
        return None