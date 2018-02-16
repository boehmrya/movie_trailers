# movie class definition
class Movie():
	def __init__(self, movieTitle, movieStoryline, posterImage, trailerYoutube, movieReleaseDate):
		self.title = movieTitle
		self.storyline = movieStoryline
		self.posterImageUrl = posterImage
		self.trailerYoutubeUrl = trailerYoutube
		self.releaseDate = movieReleaseDate

	def showTrailer(self):
		webbrowser.open(self.trailerYoutubeUrl)