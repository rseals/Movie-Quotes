#!/usr/bin/env python
import random

movies = ['Star Wars 4,5 or 6','King Pin','Good Fellas','Casino','Tombstone','Big Trouble in Little China','O Brother where art though','True Lies','The Big Lebowski','Smokey and the Bandit','Independence Day','Vacations','Dumb and Dumber','Trading places','Ghost busters I or II','Thunder dome','Die hard','Pulp fiction','Hateful eight','Caddie shack','Stripes','Airplane','Apollo 13','Breakfast club','Animal house','Better off dead','Almost heros','Cabin boy','Young Frankenstein','Blazing saddles','Friday','Bull Durham','Romancing the Stone','Beverly Hills Cop','Fletch','Revenge of the Nerds','Step Brothers','talladega nights','Anchorman','Top Gun','Full metal jacket','Hunt for red October','Silence of the Lambs','Raising Arizona','Back to the future trilogy','Mall rats','Rocky universe','Shawshank redemption','Cool hand luke','So I married an axe murderer','Dodgeball','Sixteen Candles']

numberofmovies = len(movies)

print ("Number of movies in the database: " + str(numberofmovies))
print ("<br>")
secure_random = random.SystemRandom()
print("Your movie quote challenge is: " + secure_random.choice(movies))

