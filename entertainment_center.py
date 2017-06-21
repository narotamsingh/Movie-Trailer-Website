import media
import fresh_tomatoes
"""
This Create multiple instances of Python Class (Movie from media) to represent
favorite movies; group all the instances together in a list. Then called a
function open_movies_page that takes in a argument, which is a list of movies,
and creates an HTML file which will display all of favorite movies.
"""


# String to hold part of poster URL.
wiki_url = "https://upload.wikimedia.org/wikipedia/en/"

noor = media.Movie(
    "Noor",
    "Noor is an Indian comedy-drama film that features Sonakshi\
    Sinha in the lead titular role.",
    wiki_url+"c/c1/Noor_Poster.jpg",
    "https://www.youtube.com/watch?v=DHuM6C6EyXE")

llb = media.Movie(
    "Jolly LLB 2",
    "Indian black comedy film, A courtroom drama which\
    satirizes the notion of the Indian legal system.",
    wiki_url+"4/4b/Jolly_LLB_2_first_look.jpg",
    "https://www.youtube.com/watch?v=-T4ESR1aGUo")
ok = media.Movie(
    "Ok Jaanu",
    "Indian romantic drama film, a young couple in a \
    live-in relationship in Mumbai with an older couple.",
    wiki_url+"b/b8/Ok_Jaanu_poster.jpg",
    "https://www.youtube.com/watch?v=eNTAj6J1mcU")
kaabil = media.Movie(
    "Kaabil",
    "Indian Hindi-language action thriller film. It features\
    a love affair between two blind people.",
    wiki_url+"c/ce/Kaabil_Movie_Poster.jpg",
    "https://www.youtube.com/watch?v=O65JHeSDhuc")
half_gf = media.Movie(
    "Half Girlfriend",
    "Half Girlfriend is an Indian romantic drama film based\
    on the novel of same name written by Chetan Bhagat.",
    wiki_url+"6/6e/Half_Girlfriend_Poster.jpg",
    "https://www.youtube.com/watch?v=KmlBnmyelHI")
badrinath = media.Movie(
    "Badrinath Ki Dulhania",
    "Indian romantic comedy film, marks the second\
    installment of a franchise that began with Humpty \
    Sharma Ki Dulhania.",
    wiki_url+"7/76/Badrinath_Ki_Dulhania_Cover.jpg",
    "https://www.youtube.com/watch?v=1YBl3Zbt80A")

# Group all the instances together in a list
movies = [noor, llb, ok, kaabil, half_gf, badrinath]

# Function called open_movies_page from starter code repository that contains
# a Python module called fresh_tomatoes.py that takes in one argument, which
# is a list of movies, and creates an HTML file which will display all of
# favorite movies.
fresh_tomatoes.open_movies_page(movies)
