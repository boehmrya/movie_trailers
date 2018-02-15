
import fresh_tomatoes
import media
import requests
import json


# present options to user to pick a genre
print("Enter a number for a genre: ")
genre = int(input("[1]Action [2]Adventure [3]Animation [4]Comedy [5]Crime : "))


# translate genre to genreId to use in moviedb request
if genre == 1:
	genreId = 28 # action
elif genre == 2:
	genreId = 12 # adventure
elif genre == 3:
	genreId = 16 # animation
elif genre == 4:
	genreId = 35 # comedy
else:
	genreId = 80 # crime is default


# present option on how many movies to show
# keep asking until the user enters a valid number
totalMovies = 0
while totalMovies < 1 or totalMovies > 20:
	totalMovies = int(input("Enter the number of movies to display (between 1 and 20): "))
	if totalMovies < 1 or totalMovies > 20:
		print("Sorry, you must enter a number between 1 and 20")


# make request to themoviedb.org
req = requests.get("https://api.themoviedb.org/3/discover/movie?api_key=a480f73de28772662beca0b5fab53f97&language=en-US&sort_by=popularity.desc&with_genres=" + str(genreId))


# build python dictionary
movieDict = json.loads(req.text)

 
# create movies and build movie list from api data
i = 0
movies = []
while i < totalMovies:
	# movie
	thisMovie = movieDict['results'][i]

	# build first three fields
	title = thisMovie['title']
	storyline = thisMovie['overview']
	posterUrl = "https://image.tmdb.org/t/p/w200" + thisMovie['poster_path']

	# get video url
	movieId = thisMovie['id']
	videoReq =requests.get("http://api.themoviedb.org/3/movie/" + str(movieId) + "/videos?api_key=a480f73de28772662beca0b5fab53f97&language=en-US")
	videoDict = json.loads(videoReq.text)
	videoKey = videoDict['results'][0]['key']
	videoUrl = "https://www.youtube.com/watch?v=" + str(videoKey)

	# create movie
	newMovie = media.Movie(title, storyline, posterUrl, videoUrl)
	movies.append(newMovie)

	# move to next movie
	i += 1


# open brower window
fresh_tomatoes.open_movies_page(movies)

