
import fresh_tomatoes
import media


# create movies
fewGoodMen = media.Movie("A Few Good Men", 
						"A story of justice for two marines",
						"https://upload.wikimedia.org/wikipedia/en/4/45/A_Few_Good_Men_poster.jpg",
						"https://www.youtube.com/watch?v=ePo91pMcu94")

lalaLand = media.Movie("La La Land", 
						"Sebastian and Mia are drawn together by their common desire to do what they love.",
						"https://upload.wikimedia.org/wikipedia/en/a/ab/La_La_Land_%28film%29.png",
						"https://www.youtube.com/watch?v=0pdqf4P9MB8")

avengers = media.Movie("The Avengers", 
						"Nick Fury, director of S.H.I.E.L.D., initiates a superhero recruitment effort to defeat the unprecedented threat to Earth.",
						"https://upload.wikimedia.org/wikipedia/en/thumb/f/f9/TheAvengers2012Poster.jpg/220px-TheAvengers2012Poster.jpg",
						"https://www.youtube.com/watch?v=NPoHPNeU9fc")

deadpool = media.Movie("Deadpool", 
						"With help from mutant allies, Deadpool uses his new skills to hunt down the man who nearly destroyed his life.",
						"https://upload.wikimedia.org/wikipedia/en/thumb/4/46/Deadpool_poster.jpg/220px-Deadpool_poster.jpg",
						"https://www.youtube.com/watch?v=ONHBaC-pfsk")

goneGirl = media.Movie("Gone Girl", 
						"when Amy goes missing on the couple's fifth wedding anniversary, Nick becomes the prime suspect in her disappearance.",
						"https://upload.wikimedia.org/wikipedia/en/0/05/Gone_Girl_Poster.jpg",
						"https://www.youtube.com/watch?v=Ym3LB0lOJ0o")


dumbAndDumber = media.Movie("Dumb and Dumber", 
						"Harry and Lloyd go to Aspen.",
						"https://upload.wikimedia.org/wikipedia/en/thumb/6/64/Dumbanddumber.jpg/220px-Dumbanddumber.jpg",
						"https://www.youtube.com/watch?v=l13yPhimE3o")

			
# list of movies
movies = [fewGoodMen, lalaLand, avengers,  deadpool, goneGirl, dumbAndDumber]


# open brower window
fresh_tomatoes.open_movies_page(movies)

