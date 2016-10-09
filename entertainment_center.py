
import media
import fresh_tomatoes

star_trek_reboot = media.Movie("Star Trek (2009)",
                        "An alternate timeline of the crew of the USS Enterprise venturing where no man has gone before",
                        "https://upload.wikimedia.org/wikipedia/en/2/29/Startrekposter.jpg",
                        "https://www.youtube.com/watch?v=b8YxTPVkeBE")

star_wars = media.Movie("Star Wars: Episode IV - A New Hope",
                     "A long time ago, in a galaxy far, far away - a classic space epic",
                     "https://upload.wikimedia.org/wikipedia/en/8/87/StarWarsMoviePoster1977.jpg",
                     "https://www.youtube.com/watch?v=vP_1T4ilm8M")

red_october = media.Movie("The Hunt for Red October",
                          "The hunt for a rogue Soviet nuclear submarine",
                          "https://upload.wikimedia.org/wikipedia/en/3/36/The_Hunt_for_Red_October_movie_poster.png",
                          "https://www.youtube.com/watch?v=Ktky-5jjf7E")

independence_day = media.Movie("Independence Day",
                               "We are not alone, and the aliens aren't friendly",
                               "https://upload.wikimedia.org/wikipedia/en/b/bb/Independence_day_movieposter.jpg",
                               "https://www.youtube.com/watch?v=B1E7h3SeMDk")

sense_sensibility = media.Movie("Sense and Sensibility",
                                "Lose your heart and come to your senses",
                                "https://upload.wikimedia.org/wikipedia/en/6/69/Sense_and_sensibility.jpg",
                                "https://www.youtube.com/watch?v=lJrAZeP_8tA")

four_weddings = media.Movie("Four Weddings and a Funeral",
                            "Over the course of five social occasions, a committed bachelor must consider the notion that he may have discovered love",
                            "https://upload.wikimedia.org/wikipedia/en/3/35/Four_weddings_poster.jpg",
                            "http://www.imdb.com/title/tt0109831/?ref_=nv_sr_1")

movies = [star_trek_reboot, star_wars, red_october, independence_day,
          sense_sensibility, four_weddings]

fresh_tomatoes.open_movies_page(movies)



