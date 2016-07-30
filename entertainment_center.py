import media
import fresh_tomatoes

toy_story = media.Movie(
    "Toy Story", 
    "A story of a boy and his toys that come to life",
    "http://a.dilcdn.com/bl/wp-content/uploads/sites/8/2013/02/toy_story_wallpaper_by_artifypics-d5gss19.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie(
    "Avatar", 
    "A marine on an alien planet",
    "http://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jp",
        "https://www.youtube.com/watch?v=5PSNL1qE6VY")
batman_vs_superman = media.Movie(
    "Batman v Superman: Dawn of Justice", 
    "Batman believes Superman is a huge threat for the Earth",
    "http://images.fandango.com/images/fandangoblog/the-hidden-plot-of-batman-vs-superman-dawn-of-justice-593860.jpg",                              
    "https://www.youtube.com/watch?v=fis-9Zqu2Ro")
civil_war = media.Movie(
    "Captain America: Civil War",
    "Captain America against the Iron Man",
    "http://t2.gstatic.com/images?q=tbn:ANd9GcQJHE0wTHT_pNRdZlnJj5IkzF49uMF3be1gfIIKw8A8z_3oHVRO",
    "https://www.youtube.com/watch?v=dKrVegVI0Us")
star_wars = media.Movie(
    "Star Wars: The Force Awakens", 
    "The next episode of the Star Wars",
    "http://vignette2.wikia.nocookie.net/starwars/images/f/fd/Star_Wars_Episode_VII_The_Force_Awakens.jpg/revision/latest/scale-to-width-down/500?cb=2\
0151018162823",
    "https://www.youtube.com/watch?v=sGbxmsDFVnE")
fight_club = media.Movie(
    "Fight Club", 
    "A depressed man suffering from insomnia meets a strange soap salesman\
 named Tyler Durden",
    "http://www.gstatic.com/tv/thumb/movieposters/23069/p23069_p_v8_ad.jpg",
    "https://www.youtube.com/watch?v=SUXWAEX2jlg")

# create a list of all Movie objects
movies = [
    toy_story, avatar, 
    batman_vs_superman, civil_war, 
    star_wars, fight_club] 
# open a Movie Trailer Site
fresh_tomatoes.open_movies_page(movies)                                       
