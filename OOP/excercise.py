# Design and implement a Python program that models a music playlist using object-oriented programming concepts. The program should define appropriate classes and include methods for managing songs within a playlist.
# Create a Song class that includes the following attributes
# Title,Artist,Duration (in minutes)
# Create a Playlist class that includes:
# A name for the playlist
# A list to store added Song objects
# Implement the following methods in the Playlist class:
# add_song(song): Adds a song to the playlist.
# remove_song(title): Removes a song from the playlist by title.
# total_duration(): Calculates and returns the total duration of all songsshow_playlist()
# Displays all songs currently in the playlist in a formatted list.

class Song:
    count = 0
    all_songs = None
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration
        if Song.all_songs is None:
            self.all_songs = []
        else:
            self.all_songs = Song.all_songs
            Song.count += 1
        
    def __str__(self):
        return f"{self.title}"
    # \nArtist: {self.artist}\nDuration: {self.duration}\n"
        
        
class Playlist(Song):
    song_count = 0
    def __init__(self, playlist_name='Default', added_songs=None): 
        self.playlist_name = playlist_name
        if added_songs is None:            
            self.added_songs = []
        else:
            self.added_songs = added_songs
        
    def add_song(self, song):
        if song not in self.added_songs:
            self.added_songs.append(song)
            Playlist.song_count += 1
        
    def remove_song(self, song):
        for song in self.added_songs: 
            self.added_songs.remove(song)
            Playlist.song_count -= 1
            break        
        
    def __str__(self):
        playlist_songs = ""
        for item in self.added_songs:
            playlist_songs += item.__str__() + "\n"  
            # playlist_songs += str(item)        
        return f"{self.playlist_name} music\n{playlist_songs}"
    
song1 = Song("Freu", "Nehy", 1)
song2 = Song("Heyy", "Kelly", 2)
song3 = Song("Luiou", "Jdut", 3)            
song4 = Song("Luiou", "Jdut", 3)            
# song4 = Song("Luiou", "JUYt", 4)            
# song4 = Song("Luiou", "JUYt", 4)            
# print(song1.get_song())
# print(song1)
# print(song2)
playlist1 = Playlist("Kenyan")
playlist1.add_song(song1)
playlist1.add_song(song2)
# playlist1.remove_song("Freu")
playlist1.add_song(song3)
playlist1.add_song(song4)

playlist2 = Playlist("Ugandan")
playlist2.add_song(song1)
playlist2.add_song(song2)
# playlist2.remove_song("Freu")
playlist2.add_song(song3)
playlist2.add_song(song4)



# print(Song.count)
# print(playlist2.song_count)
# print(playlist1.title)
print (playlist1)
print (playlist2)
# print (playlist1.show_list())
# print (playlist2.added_songs)
# print()