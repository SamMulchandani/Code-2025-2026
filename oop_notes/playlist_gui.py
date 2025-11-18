from nicegui import ui
from playlist import Playlist

def open_playlist():
    playlist.load(f"oop_notes/{open_filename_input.value}")

    output_box.value = str(playlist)
    open_dialog.close()

def save_playlist():
    playlist.save(f"oop_notes/{save_filename_input.value}")

    save_dialog.close()

def search():
    search_dialog.open()

    if ", " in search_input.value:
        song = search_input.value.split(", ")
        title = song[0]
        artist = song[1]
        result = playlist.find_song_from_info(title, artist)

        if result is not None:    
            title_label.text = f"Title: {result.title}"
            artist_label.text = f"Artist: {result.artist}"
            album_label.text = f"Album: {result.album}"
        else:
            search_dialog.close()
            ui.notify(f"Song not found...")
            
    else:
        search_dialog.close()
        ui.notify("Please format search \"title, artist\"")

def edit():
    song = search_input.value.split(", ")
    title = song[0]
    artist = song[1]

    playlist.find_song_and_edit_info(title, artist, edit_title_input.value, edit_artist_input.value, edit_album_input.value)
    
    edit_dialog.close()
    search_dialog.close()
    output_box.value = str(playlist)

def remove():
    song = search_input.value.split(", ")
    title = song[0]
    artist = song[1]
    removed = playlist.remove(title, artist)
    
    search_dialog.close()
    output_box.value = str(playlist)
    ui.notify(f"{removed.title} by {removed.artist} removed successfully...")

def add():
    title = add_title_input.value
    artist = add_artist_input.value
    album = add_album_input.value
    playlist.add_song_from_info(title, artist, album)

    output_box.value = str(playlist)
    add_dialog.close()

playlist = Playlist()

# Open dialog box
with ui.dialog() as open_dialog, ui.card():
    open_filename_input = ui.input("Filename:")
    with ui.row():
        close_button = ui.button("Close", on_click=lambda: open_dialog.close())
        open_button = ui.button("Open", on_click=open_playlist)

# Save dialog box
with ui.dialog() as save_dialog, ui.card():
    save_filename_input = ui.input("Filename:")
    with ui.row():
        close_button = ui.button("Close", on_click=lambda: save_dialog.close())
        save_button = ui.button("save", on_click=save_playlist)

# Menu dropdown w/ open & save
with ui.button(icon="menu"):
    with ui.menu() as menu:
        ui.menu_item(text="Open", on_click=lambda: open_dialog.open())
        ui.menu_item(text="Save", on_click=lambda: save_dialog.open())

# Edit entry box
with ui.dialog() as edit_dialog, ui.card():
    edit_title_input = ui.input("New title: ")
    edit_artist_input = ui.input("New artist: ")
    edit_album_input = ui.input("New album: ")
    
    with ui.row():
        ui.button("Cancel", on_click=lambda: edit_dialog.close())
        ui.button("Done", on_click= edit)

# Search entry box & button
with ui.row():
    search_input = ui.input(placeholder="e.g. Hello, Adele")
    search_button = ui.button(icon="search", on_click=lambda: search())

# Search dialog box
with ui.dialog() as search_dialog, ui.card():
    title_label = ui.label("Title: ")
    artist_label = ui.label("Artist: ")
    album_label = ui.label("Album: ")
    with ui.row():
        ui.button("Close", on_click=lambda: search_dialog.close())
        ui.button("Edit", on_click=lambda: edit_dialog.open())
        ui.button("Delete", on_click= remove)


# Output box
output_box = ui.textarea(placeholder="Playlist")


# Add song dialog box
with ui.dialog() as add_dialog, ui.card():
    add_title_input = ui.input("Title: ")
    add_artist_input = ui.input("Artist: ")
    add_album_input = ui.input("Album: ")
    with ui.row():
        close_button = ui.button("Close", on_click=lambda: add_dialog.close())
        add_button = ui.button("Add", on_click=add)

# Add song button
add_button = ui.button(icon="playlist_add", on_click=lambda: add_dialog.open())


dark = ui.dark_mode().enable()
ui.run(port=23000)
# ui.run()
