# Movie Trailer Website
This site pulls in data from themoviedb.org and displays a list of movies on a webpage.  Users can click on the movie poster to play the movie trailer in a modal.  The site is written in python3 and uses bootstrap and jquery.

## Usage
run `python3 entertainment_center.py` from the root of the movie_trailers directory.  The program will prompt the user
for the movie genre and number of movies to display, and then open a browser window and display the data.  The movies will be listed in order of popularity (as determined by themoviedb.org's own ratings)

## Dependencies
You must install the following python modules before running:

* json
* request
* os
* re
* webbrowser
