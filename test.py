while True:

    print("=========Notes App=========")

    print(1, "Add Note")
    print(2, "View Notes")
    print(3, "Delete Note")
    print(4, "Exit")

    try:
        user_input = int(input("Enter your choice: "))
        if user_input == 1:
            user_note = input("Enter your note: ")
            with open("notes.txt", "a") as file:
                file.write(user_note + "\n")
            print("Note saved!")

        elif user_input == 2:
            print("View Notes")
            try:
                with open("notes.txt", "r") as file:
                    notes = file.readlines()
                    for number, note in enumerate(notes, start=1):
                        print(f"{number}: {note.strip()}")
            except FileNotFoundError:
                print("No notes found, try adding some!")

        elif user_input == 3:
            print("Delete Note")
            with open("notes.txt", "w") as file:
                pass
            print("All notes deleted!")

        elif user_input == 4:
            print("Exit")
            break

        else:
            print("Invalid choice.... Enter a number between 1 and 4!!!")
    
    except ValueError:
        print("Invalid input.... Enter a number between 1 and 4!!!")