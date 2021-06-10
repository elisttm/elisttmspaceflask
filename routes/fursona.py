from __main__ import app, flask, a
import os
from data.art import art

# 		========================

class eli():

	info = [
		"kitty",
		"minor",
		"male he/him",
		"4'8\"",
		"probably smells like seafood",
		"gremlin creature",
	]

# 		========================

@app.route('/eli')
def fursona(): 
	return flask.render_template('eli.html', eli = eli(), a = a)

@app.route('/eli/art')
def eli_art():
	return flask.render_template('eliart.html', art = art(), eli = eli(), a = a) #fuckyou = flask.Markup(fuckyou)

@app.route('/gallery')
def gallery():
	return flask.render_template('eliart.html', art = art(), eli = eli(), a = a)