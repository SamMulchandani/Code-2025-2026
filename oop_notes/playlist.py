from song import Song
class Playlist:
    def __init__(self):
        self.songs = []

    def __str__(self):
        s = ""
        for song in self.songs:
            s += str(song) + "\n"
        return s
    
    def add_song_from_info(self, title, artist, album):
        self.songs.append(Song(title,artist,album))

    def load(self, filename):
        self.songs = []
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                song = Song(parts[0], parts[1], parts[2])
                self.songs.append(song)

    def save(self, filename):
        with open(filename, "w") as file:
            for song in self.songs:
                file.write(f"{song.title},{song.artist},{song.album}\n")

# currents = Playlist()
# currents.load("oop_notes/album.csv")
# print(currents)