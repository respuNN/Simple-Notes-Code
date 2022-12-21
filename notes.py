import os

# Function to display the menu and get the user's choice
def show_menu():
    print('1. Show all notes')
    print('2. Add a new note')
    print('3. Edit a note')
    print('4. Delete a note')
    print('5. Quit')
    choice = input('Enter your choice: ')
    return int(choice)

# Function to show all notes
def show_all_notes():
    # Read the notes from the file
    with open('notes.txt', 'r') as f:
        notes = f.readlines()

    # Print the notes
    for i, note in enumerate(notes):
        print(f'{i+1}. {note}')

# Function to add a new note
def add_note():
    # Get the note from the user
    note = input('Enter your note: ')

    # Add the note to the file
    with open('notes.txt', 'a') as f:
        f.write(note + '\n')

# Function to edit a note
def edit_note():
    # Show all notes
    show_all_notes()

    # Get the index of the note to edit
    index = int(input('Enter the index of the note to edit: '))

    # Read all the notes from the file
    with open('notes.txt', 'r') as f:
        notes = f.readlines()

    # Replace the note at the specified index
    new_note = input('Enter the new note: ')
    notes[index-1] = new_note + '\n'

    # Write the updated notes to the file
    with open('notes.txt', 'w') as f:
        f.writelines(notes)

# Function to delete a note
def delete_note():
    # Show all notes
    show_all_notes()

    # Get the index of the note to delete
    index = int(input('Enter the index of the note to delete: '))

    # Read all the notes from the file
    with open('notes.txt', 'r') as f:
        notes = f.readlines()

    # Delete the note at the specified index
    del notes[index-1]

    # Write the updated notes to the file
    with open('notes.txt', 'w') as f:
        f.writelines(notes)

# Create the notes file if it doesn't exist
if not os.path.exists('notes.txt'):
    open('notes.txt', 'w').close()

# Main loop
while True:
    # Show the menu and get the user's choice
    choice = show_menu()

    # Take the appropriate action based on the user's choice
    if choice == 1:
        show_all_notes()
    elif choice == 2:
        add_note()
    elif choice == 3:
        edit_note()
    elif choice == 4:
        delete_note()
    elif choice == 5:
        break