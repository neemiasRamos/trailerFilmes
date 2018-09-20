import webbrowser
#classe Movie
class Movie():
    #construtor
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        #variaveis do objeto
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    #método do objeto
    def show_trailer(self):
        #acessa o navegador e abre o link da variavel do objeto self.trailer_youtube_url
        webbrowser.open(self.trailer_youtube_url)

    
