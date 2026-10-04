import json

database = {}

try:
    with open("data.json", "r") as file:
        database = json.load(file)
except FileNotFoundError:
    pass

while True:
    user = input("db> ").strip()

    if user == "":
        continue

    parts = user.split(maxsplit=2)
    command = parts[0].upper()

    if command == "EXIT":
        break

    elif command == "SET":
        if len(parts) != 3:
            print("Usage: SET <key> <value>")
        else:
            database[parts[1]] = parts[2]
            print("Value saved.")

    elif command == "GET":
        if len(parts) != 2:
            print("Usage: GET <key>")
        elif parts[1] in database:
            print(database[parts[1]])
        else:
            print("Key not found.")

    elif command == "DEL":
        if len(parts) != 2:
            print("Usage: DEL <key>")
        elif parts[1] in database:
            del database[parts[1]]
            print("Key deleted.")
        else:
            print("Key not found.")

    elif command == "EXISTS":
        if len(parts) != 2:
            print("Usage: EXISTS <key>")
        else:
            print(parts[1] in database)

    elif command == "SAVE":
        if len(parts) != 2:
            print("Usage: SAVE <filename>")
        else:
            with open(parts[1], "w") as file:
                json.dump(database, file, indent=4)
            print("Database saved.")

    elif command == "LOAD":
        if len(parts) != 2:
            print("Usage: LOAD <filename>")
        else:
            try:
                with open(parts[1], "r") as file:
                    loaded_data = json.load(file)

                if isinstance(loaded_data, dict):
                    database = loaded_data
                    print("Database loaded.")
                else:
                    print("Invalid database file.")
            except FileNotFoundError:
                print("File not found.")

    else:
        print("Invalid command.")