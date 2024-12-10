#Music Player

#fucntion to print the artist
class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def play(self):
        print(f"Playing '{self.title}' by {self.artist}")

    def pause(self):
        print(f"Paused '{self.title}'")

#function to fetch Playlist
class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        if isinstance(song, Song):
            self.songs.append(song)
            print(f"Added '{song.title}' to playlist '{self.name}'")
        else:
            print("Only Song instances can be added.")

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"Removed '{song.title}' from playlist '{self.name}'")
        else:
            print(f"Song '{song.title}' not found in playlist '{self.name}'")

    def play_all(self):
        if not self.songs:
            print("No songs in the playlist.")
        for song in self.songs:
            song.play()


class MusicPlayer:
    def __init__(self, playlist):
        self.current_song = None
        self.playlist = playlist

    def play(self):
        if self.current_song:
            self.current_song.play()
        else:
            print("No song is currently selected.")

    def pause(self):
        if self.current_song:
            self.current_song.pause()
        else:
            print("No song is currently selected.")

    def next(self):
        if self.playlist.songs:
            if self.current_song is None:
                self.current_song = self.playlist.songs[0]
            else:
                current_index = self.playlist.songs.index(self.current_song)
                if current_index + 1 < len(self.playlist.songs):
                    self.current_song = self.playlist.songs[current_index + 1]
                else:
                    print("You are at the last song of the playlist.")
            self.play()
        else:
            print("No songs in the playlist to play.")


# Example Usage
if __name__ == "__main__":
    song1 = Song("Song A", "Artist A")
    song2 = Song("Song B", "Artist B")

    my_playlist = Playlist("My Favorite Songs")
    my_playlist.add_song(song1)
    my_playlist.add_song(song2)

    music_player = MusicPlayer(my_playlist)

    music_player.playlist.play_all()  # Plays all songs
    music_player.next()  # Plays first song
    music_player.next()  # Plays second song
    music_player.next()  # No more songs
    music_player.pause()  # Pauses current song