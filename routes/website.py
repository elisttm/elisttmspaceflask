from __main__ import app, flask, a

# 		========================

class site():

	github = 'https://github.com/elisttm/elisttmspaceflask'

# 		========================

@app.route('/website')
def mywebsite(): 
	return flask.render_template('website.html', site = site(), a = a)
