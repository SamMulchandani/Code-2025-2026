from nicegui import ui
from roster import *


def add():
    # TODO: Get input strings from dialog box
    # TODO: Add new student to roster from strings)
    first = first_input.value
    last = last_input.value
    grade = int(grade_input.value)
    roster.add_student_by_info(first, last, grade)
    text_area.value = str(roster)

    add_student_dialog.close()

def search():
    # FIXME: empty search_box crashes search...
    full_name = search_box.value
    names = full_name.split(" ")
    first = names[0]
    last = names[1]
    
    result = roster.find(first, last)
    
    if result is not None:
        first_label.text = "First name: " + result.first
        last_label.text = "Last name: " + result.last
        grade_label.text = "Grade: " + str(result.grade)
    else:
        ui.notify(f"{first} {last} was not found...")

    search_output_dialog.open()

def open_file():
    filename = open_filename_input.value
    # filename = "oop_notes/data.csv"
    roster.load(f"oop_notes/{filename}")
    # print(filename)
    text_area.value = str(roster)

    ui.notify(f"{filename} opened successfully...")
    open_dialog.close()

def save_file():
    filename = save_filename_input.value
    roster.save(f"oop_notes/{filename}")

    ui.notify(f"{filename} saved successfully...")
    save_dialog.close()

# Creating blank roster
roster = Roster()

# Title window
ui.page_title("Roster GUI")

# Open & Save Menu:

# Open Dialog
with ui.dialog() as open_dialog, ui.card():
    open_filename_input = ui.input(label="Filename:")
    with ui.row():
        cancel_button = ui.button("Cancel", on_click=open_dialog.close)
        open_button = ui.button("Open", on_click=open_file)

# Save Dialog
with ui.dialog() as save_dialog, ui.card():
    save_filename_input = ui.input("Filename:")
    with ui.row():
        cancel_button = ui.button("Cancel", on_click=save_dialog.close)
        save_button = ui.button("Save", on_click=save_file)

# Menu
with ui.button(icon='menu'):
    with ui.menu() as menu:
        ui.menu_item('Open', on_click= open_dialog.open)
        ui.menu_item('Save', on_click= save_dialog.open)

# TODO: ... a search dialog box
with ui.dialog() as search_output_dialog, ui.card():
        first_label = ui.label("First name: ")
        last_label = ui.label("Last name: ")
        grade_label = ui.label("Grade: ")
        ui.button("Close", on_click=lambda: search_output_dialog.close())

# Search
with ui.row():
    search_box = ui.input()
    search_button = ui.button(icon= 'search', text= 'Search', on_click= search)

# TODO: Text area for output (we will fix this later)
text_area = ui.textarea("Roster")
# text_area.set_enabled(False)

# Add
add_student_button = ui.button(icon='person_add_alt', on_click= lambda: add_student_dialog.open())

# TODO: ... an add student dialog box
with ui.dialog() as add_student_dialog, ui.card():
    first_input = ui.input("First Name:")
    last_input = ui.input("Last Name:")
    grade_input = ui.input("Grade:")
    with ui.row():
        close_button = ui.button("Close", on_click= lambda: add_student_dialog.close())
        submit_button = ui.button("Submit", on_click= add)


ui.run()