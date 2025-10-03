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

    def selection_sort_by_title(self):
        front = 0
        for front in range(len(self.songs)):
            min = front
            for i in range(front, len(self.songs)):
                if self.songs[i].title < self.songs[min].title:
                    min = i
            temp = self.songs[front]
            self.songs[front] = self.songs[min]
            self.songs[min] = temp

    def bubble_sort_by_artist(self):
        for end in range(len(self.songs), 0, -1):
            for i in range(1,end):
                if self.songs[i-1].artist > self.songs[i].artist:
                    temp = self.songs[i]
                    self.songs[i] = self.songs[i-1]
                    self.songs[i-1] = temp

    def save(self, filename):
        with open(filename, "w") as file:
            for song in self.songs:
                file.write(f"{song.title},{song.artist},{song.album}\n")