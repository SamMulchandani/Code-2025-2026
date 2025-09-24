from song import Song
class Playlist:
    def __init__(self):
        self.songs = []

    def __str__(self):
        s = ""
        for song in self.songs:
            s += str(song) + "\n"
        return s

    def load(self, filename):
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                song = Song(parts[0], parts[1], parts[2])
                self.songs.append(song)

# currents = Playlist()
# currents.load("oop_notes/album.csv")
# print(currents)