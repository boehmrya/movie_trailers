# movie class definition
class Movie():
	def __init__(self, movieTitle, movieStoryline, posterImage, trailerYoutube):
		self.title = movieTitle
		self.storyline = movieStoryline
		self.posterImageUrl = posterImage
		self.trailerYoutubeUrl = trailerYoutube

	def showTrailer(self):
		webbrowser.open(self.trailerYoutubeUrl)