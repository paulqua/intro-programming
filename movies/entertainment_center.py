import media
import fresh_tomatoes


toy_story = media.Movie("Toy story", "Toys that come to life and save the day!", "http://a.dilcdn.com/bl/wp-content/uploads/sites/8/2013/02/toy_story_wallpaper_by_artifypics-d5gss19.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar", "Marines that live and work on an alien planet", "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg", "https://www.youtube.com/watch?v=5PSNL1qE6VY")

the_aviator = media.Movie("Aviator", "The story of Howard Hughes life and all his accomplishments.", "http://www.iwannawatch.to/wp-content/uploads/2011/04/The-Aviator-2004.jpg", "https://www.youtube.com/watch?v=FebPJlmgldE")

lawrence_of_arabia = media.Movie("Lawrence of Arabia", "One man does whith a few arab tribes, what England could not with the whole army.", "https://images-na.ssl-images-amazon.com/images/I/51P24W0KFHL._SY445_.jpg", "https://www.youtube.com/watch?v=zmr1iSG3RTA")

wolf_of_wall_street = media.Movie("Wolf of Wall Street", "One mans crazy story of drugs, money and power.", "https://images-na.ssl-images-amazon.com/images/M/MV5BMjIxMjgxNTk0MF5BMl5BanBnXkFtZTgwNjIyOTg2MDE@._V1_UX182_CR0,0,182,268_AL_.jpg", "https://www.youtube.com/watch?v=pabEtIERlic")

madagascar = media.Movie("Madagascar", "Funny zoo animals that escape from zoo.", "https://loftcinema.org/files/2016/04/Madagascar-movie-poster.jpg", "https://www.youtube.com/watch?v=dm-eiFVtRws")

movies = [toy_story, avatar, the_aviator, lawrence_of_arabia, wolf_of_wall_street, madagascar]
fresh_tomatoes.open_movies_page(movies)