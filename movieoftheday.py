#!/usr/bin/env python
import random
import sqlite3
from graphics import *

def databasequery():
    sqlite_file = 'movieoftheday.db'
    table_name = 'movielist'

    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    c.execute('select name from movielist order by random() limit 1;')

    movie_name = c.fetchone()
    
    return movie_name

    # c.execute('SELECT moviequotes.quote FROM movielist LEFT JOIN moviequotes ON moviequotes.movienumber = "movielist"."index" WHERE moviequotes.quote NOT NULL;')

    c.execute('select name, moviequotes.quote from movielist LEFT join moviequotes on moviequotes.movienumber = "movielist"."index" where movielist.RowID = 32 and moviequotes.quote NOT null;')

    movie_quotes = c.fetchall()

def UserInterface():
    win = GraphWin('Movie of the Day Picker', 320, 240)
    win.setBackground('Blue')
    #rec = Rectangle(Point(245,200), Point(255,75))
    #rec.setFill('brown')
    #rec.draw(win)
    #label = Text(center, "Tree")
    #label.draw(win)
    finishbuttontext = Text(Point(160,120), movie_of_the_day)
    finishbuttontext.setSize(20)
    finishbuttontext.setStyle("bold")
    finishbuttontext.setTextColor("white")
    finishbuttontext.draw(win)
 
movie_of_the_day = databasequery()
# movie_of_the_day_quote = 

UserInterface()

print ('Movie of the day is:', movie_of_the_day)
print ()
