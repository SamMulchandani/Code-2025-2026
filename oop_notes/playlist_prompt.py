from playlist import *

playlist = Playlist()

cont = True
while cont:
    print("===PLAYLIST VIEWER===\n")
    choice = input("What would you like to do?\n(a)dd song\n(o)pen file\n(so)rt\n(s)ave file\n(v)iew songs\n(q)uit program\n>>> ")

    if choice == "a":
        title = input("Title? ")
        artist = input("Artist? ")
        album = input("Album? ")
        playlist.add_song_from_info(title,artist,album)
        print("Song added successfully...\n")

    elif choice == "o":
        filename = input("\nWhat file do you want to open?\n")
        playlist.load(f"oop_notes/{filename}")
        print(f"{filename} loaded successfully...\n")

    elif choice == "so":
        sort_type = input("Sort by what?\n(a)rtist\n(t)itle\n")
        if sort_type == "a":
            playlist.bubble_sort_by_artist()
        elif sort_type == "t":
            playlist.selection_sort_by_title()
        else:
            "Invalid choice...\n"
        print("Playlist sorted successfully...\n")


    elif choice == "s":
        save_file = input("Save to where? ")
        playlist.save(f"oop_notes/{save_file}")

    elif choice == "v":
        print("\nViewing songs...")
        print(playlist)
        print()

    elif choice == "q":
        cont = False
    else:
        print("Invalid choice...")