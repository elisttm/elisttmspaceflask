from __main__ import app, flask, a
import os
from data.art import art
from datetime import datetime

# 		========================

class eli():

	info = [
		"kitty",
		"minor",
		"male he/him",
		"4'8\"",
		"probably smells like seafood",
		"gremlin creature",
		"can be drawn with clothes!",
		"ear fluff is entirely optional",
	]

# 		========================

@app.route('/eli')
def fursona(): 
	return flask.render_template('eli.html', eli = eli(), a = a)

@app.route('/eli/art')
def eli_art():
	return flask.render_template('eliart.html', art = art().art_, eli = eli(), a = a) #fuckyou = flask.Markup(fuckyou)

@app.route('/eli/art/newest')
def eli_art_newest():
	return flask.render_template('eliart.html', art = art().sorted_art, eli = eli(), a = a, sorted_ = True) #fuckyou = flask.Markup(fuckyou)
