import json

from datetime import datetime

FILENAME = "notes.json"

def load_notes():
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return[]
    
def save_notes(notes):
    with open(FILENAME, "w",  encoding="utf-8") as f:
        json.dump(notes, f, indent=4, ensure_ascii=False)

def show_menu():
    print("MENU")
    print("1.add note")
    print("2.show all notes")
    print("3.search")
    print("4.delete note")
    print("5.edit note")
    print("6.statistic")
    print("0.exit")

def add_notes(notes):

    title = input("title: ")
    body = input("body text: ")
    created_time = datetime.now().strftime("%Y-%m-%d %H:%M%:%S")

    note = {
        "title":title,
        "body":body,
        "created_time":created_time
    }

    notes.append(note)
    

def list_notes(notes):
    if not notes:
        print(" no notes ")
        return 
    print("ALL NOTES:")
    print()


def search_notes(notes):
    pass


def delete_notes(notes):
    pass

def edit_notes(notes):
    pass

def statistic(notes):
    pass

def main():
    notes = load_notes()
    while True:
        show_menu()
        choice = input("chooce the number: ")
        if choice == "1":
            add_notes(notes)
        elif choice == "2":
            list_notes(notes)
        elif choice == "3":
            search_notes(notes)
        elif choice == "4":
            delete_notes(notes)
        elif choice == "5":
            edit_notes(notes)
        elif choice == "6":
            statistic(notes)
        elif choice == "0":
            save_notes(notes)
            break

if __name__ == "__main__":
    main()

            

