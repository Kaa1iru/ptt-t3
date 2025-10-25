# Python Record Manager
[T3-TECHNICAL] Test Cases

A simple command-line record manager built with Python.  
This program allows users to add, update, search, and remove record interactively.

# Installation
1. Clone the repository to your computer.
```bash
git clone https://github.com/Kaa1iru/ptt-t3.git
```
2. Navigate to the repository
```bash
cd ptt-t3
```
3. Run the `main.py` file.
```bash
python3 main.py
```

# Usage
Upon running the app, the user will be prompted to choose one out the four functions.

- Add Record
    - The user have to input the record's title, then it will be appended to the database file.
- Search Record
    - Prompts the user to choose if the user want to search by ID or name. Then it will display the searched record.
- Update Record
    - Prompts the user to enter the ID of the record, then the user will be prompt again to enter the new title of the record.
- Delete Record
    - Prompts the user to enter the ID of the record, then it will be removed from the database file.
- Exit
    - It will simply terminate the program.

### Notes
These system uses 2 .txt files. `database.txt` for the data storage, it contains the ID and record title. And a `counter.txt` that contains the latest ID value which will be used for producing unique IDs and prevent duplications.

`database.txt` and `counter.txt` is automatically created if it doesn't exist.
