import webbrowser

class Movie(object):
    '''This class provides a way to store movie related info'''
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):            
        self.title = movie_title
        self.story_line = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):     
        '''open a trailer url in a browser'''
        webbrowser.open(self.trailer_youtube_url)
        webbrowser.open(self.trailer_youtube_url)