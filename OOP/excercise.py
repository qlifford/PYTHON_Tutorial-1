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
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration
        self.all_songs = Playlist.added_songs
            
    def __str__(self):
        self.all_songs      
        
class Playlist(Song):
    def __init__(self, playlist_name='Default'): 
        self.playlist_name = playlist_name
        self.added_songs = []

        
    def add_song(self, title, artist, duration):
        song = (title, artist, duration)
        self.added_songs.append(song)
        Song.count += 1
        
    def remove_song(self, title):
        for song in self.added_songs: 
            if song == self.added_songs[0]:
                self.added_songs.remove(song)
                Song.count -= 1
            break        
        
    def show_list(self):
        return f"{self.playlist_name}:\n{self.added_songs}"
            
playlist1 = Playlist("Ugandan")
playlist2 = Playlist("Kenyan")

playlist1.add_song("Bet", "Medi", 2)
playlist1.add_song("Bund", "Obor", 2)
playlist1.add_song("yot", "Lucy", 2)

playlist2.add_song("hoy", "Kelly", 2)
playlist2.add_song("Loy", "Hunnyd", 2)
playlist2.add_song("KIl", "Yoto", 2)

# print(Playlist.count)
# playlist1.remove_song("Bet")
# playlist1.remove_song("Bund")
# playlist2.remove_song("KIl")
# print(Playlist.count)
# print(playlist1.count)
# print (playlist1.playlist_name)
print (playlist1.show_list())
print (playlist2.added_songs)
print()