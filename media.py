import webbrowser
"""
This is a Data structure (i.e. a Python Class) to store favorite movies, including movie title,
story line, poster URL and a YouTube link to the movie trailer.
"""

class Movie():
    #  Constructor for the movie class to create instances of movie
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
