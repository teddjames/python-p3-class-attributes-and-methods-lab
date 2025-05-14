class Song:
    # Class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        # Instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Update class-level data
        Song.add_song_to_count()
        Song.add_to_genres(self)
        Song.add_to_artists(self)
        Song.add_to_genre_count(self)
        Song.add_to_artist_count(self)

    @classmethod
    def add_song_to_count(cls):
        """
        Increment the total count of Song instances.
        """
        cls.count += 1

    @classmethod
    def add_to_genres(cls, song):
        """
        Add a song's genre to the list of genres (no duplicates).
        """
        if song.genre not in cls.genres:
            cls.genres.append(song.genre)

    @classmethod
    def add_to_artists(cls, song):
        """
        Add a song's artist to the list of artists (no duplicates).
        """
        if song.artist not in cls.artists:
            cls.artists.append(song.artist)

    @classmethod
    def add_to_genre_count(cls, song):
        """
        Track the number of songs per genre in a histogram.
        """
        genre = song.genre
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, song):
        """
        Track the number of songs per artist in a histogram.
        """
        artist = song.artist
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

# Example usage:
# Creating some songs
song1 = Song("99 Problems", "Jay-Z", "Rap")
song2 = Song("Halo", "Beyonce", "Pop")
song3 = Song("Crazy in Love", "Beyonce", "Pop")

# Inspecting class-level data
print(Song.count)          # => 3
print(Song.genres)         # => ['Rap', 'Pop']
print(Song.artists)        # => ['Jay-Z', 'Beyonce']
print(Song.genre_count)    # => {'Rap': 1, 'Pop': 2}
print(Song.artist_count)   # => {'Jay-Z': 1, 'Beyonce': 2}
