import os

file_name = "database.txt"
counter_file = "counter.txt"
separator = "=========================="
invalid = "Error: Invalid Input!"

def Search(file, search_by, search_key):
    found = False
    with open(file_name, "r") as file:
        database = file.read().strip()
        record = database.split("\n")
        # ID
        if search_by == '1':
            for i in range(len(record)):
                if record[i] == f"{int(search_key):04d}":
                    print(separator)
                    print(f"ID: {record[i]}")
                    print(f"Name: {record[i+1]}")
                    found = True
        # Name
        elif search_by == '2':
            for i in range(len(record)):
                if search_key.lower() in record[i].lower():
                    print(separator)
                    print(f"ID: {record[i-1]}")
                    print(f"Name: {record[i]}")
                    found = True

    if not found:
        print("Record does not exist.")

def Add(name):
    records = []
    with open(counter_file, "r") as file:
        lines = file.readlines()
        for i in lines:
            records.append(i.strip())

    latest_id = 0

    for i in range(len(records)):
        latest_id += 1

    latest_id += 1

    with open(file_name, "a") as file:
        file.write(separator + "\n")
        file.write(f"{latest_id:04d}\n")
        file.write(name + "\n")

    with open(counter_file, "a") as file:
        file.write(f"{latest_id}\n")

def Update():
    print(separator)
    update_id =  input("Enter ID to be updated: ").strip()

    if not update_id.isdigit():
        print(invalid)
        return

    found = False
    with open(file_name, "r") as file:
        records = file.read().strip().split("\n")

    for i in range(len(records)):
        if records[i] == update_id or records[i] == f"{int(update_id):04d}":
            print(separator)
            print(f"Current Name: {records[i+1]}")
            print("Leave Blank to Keep Current Name")
            new_name = input("Enter new name: ").strip()

            if new_name == "":
                new_name = records[i+1]

            records[i+1] = new_name
            found = True
            break

    if found:
        with open(file_name, "w") as file:
            for line in records:
                file.write(line + "\n")
        print("Record updated sucessfully!")
    else:
        print("Record does not exist.")

def Delete(id):
    records = []
    with open(file_name, "r") as file:
        lines = file.readlines()
        for i in lines:
            records.append(i.strip())

    temp = []
    found = False
    for i in range(len(records) - 2):
        if records[i] == separator:
            if records[i + 1] != f"{int(id):04d}":
                temp.append(separator)
                temp.append(records[i + 1])
                temp.append(records[i + 2])
            else:
                found = True

    with open(file_name, "w") as file:
        for line in temp:
            file.write(line + "\n")

    if found:
        print(f"ID {id} deleted successfully!")
    else:
        print(f"ID {id} not found.")

def main():
    if not os.path.exists(file_name):
        open(file_name, "w").close()
    if not os.path.exists(counter_file):
        open(counter_file, "w").close()

    while True:
        print("+------------------------+")
        print("    [1] Add Record")
        print("    [2] Search Record")
        print("    [3] Update Record")
        print("    [4] Delete Record")
        print("    [5] Exit")
        print("+------------------------+")
        choice = input("Select an option: ")

        match choice:
            case '1':
                name = input("Enter Name: ")
                if (name == ''):
                    print("Error: Name cannot be empty!")
                    continue
                elif (name.isalnum()):
                    Add(name)
                    print(f"{name} successfully added!")
                else:
                    print("Error. Name must be only alphanumeric characters.")

            case '2':
                searchBy = input("Search by: [1] ID or [2] Name: ")
                # ID
                if searchBy == '1':
                    while True:
                        try:
                            searchID = int(input("Enter ID: "))
                            break
                        except: print(invalid)
                    Search(file_name, searchBy, searchID)

                # Name
                elif searchBy == '2':
                    searchName = input("Enter name: ")
                    if searchName.strip() == '':
                        print("Error: Name cannot be empty!")
                    else:
                        Search(file_name, searchBy, searchName)

                else:
                    print(invalid)

            case '3':
                Update()
                pass

            case '4':
                delete_id = input("Enter ID: ")
                Delete(delete_id)

            case '5':
                print("Goodbye!")
                break

            case _:
                print(invalid)

main()
