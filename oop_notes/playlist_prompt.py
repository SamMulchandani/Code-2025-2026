from playlist import *

playlist = Playlist()

cont = True
while cont:
    print("===PLAYLIST VIEWER===\n")
    choice = input("What would you like to do?\n(o)pen file\n(v)iew songs\n(q)uit program\n")

    if choice == "o":
        filename = input("\nWhat file do you want to open?\n")
        print("Opening file...")
        playlist.load(filename)
        print(f"{filename} loaded successfully...")

    elif choice == "v":
        print("\nViewing songs...")
        print(playlist)

    elif choice == "q":
        cont = False