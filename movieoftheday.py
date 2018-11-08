#!/usr/bin/env python
import random
import sqlite3
from graphics import *

def databasequery():
    sqlite_file = 'movieoftheday.db'
    table_name = 'movielist'

    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    c.execute('select * from movielist order by random() limit 1;')

    movie_name = c.fetchone()
    
    return movie_name

    # c.execute('SELECT moviequotes.quote FROM movielist LEFT JOIN moviequotes ON moviequotes.movienumber = "movielist"."index" WHERE moviequotes.quote NOT NULL;')

    # movie_quotes = c.fetchall()

 
movie_of_the_day = databasequery()

print ('Movie of the day is:', movie_of_the_day)
print ('')
