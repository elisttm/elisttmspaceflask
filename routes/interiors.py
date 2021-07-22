from __main__ import app, flask, a
import os

# 		========================

# this is not a main site page i just have this for a silly business i run on a minecraft smp server

class interior():

	rules = (
		"you are allowed to specify what content you want me to decorate with, but if you decide not to or are vague i can and will take artistic liberties",
		"you are to specify the area i am to decorate. if you are vague, do not be mad if i \"overdo it\"",
		"i can and will plaster my likeness around my given work area because i think its funny",
		"you are allowed to cancel the service at any point in the process",
		"payment is required if i ask for it, although most of the time i do jobs for free",
	)

	x = "/static/images/interiors/"

	images = (
		f"{x}trick.png",
		f"{x}tes.png",
		f"{x}mossrag.png",
		f"{x}mine.png",
	)

# 		========================

@app.route('/interiors')
def interiors(): 
	return flask.render_template('interiors.html', interior = interior(), a = a)