from __main__ import app, flask, a

# 		========================

@app.route('/sitemap')
def sitemap(): 
	return flask.render_template('sitemap.html', a = a)

@app.route('/styles')
def style(): 
	return flask.render_template('extra/style.html', no_analytics = True, rickroll = "https://www.youtube.com/watch?v=dQw4w9WgXcQ", a = a)

#			-----  FUNNY  -----

@app.route('/lol', defaults={'subpage': None})
@app.route('/lol/<subpage>')
def tags(subpage):
	if not subpage: subpage = 0
	return flask.render_template('yeah.html', subpage = subpage, a = a)

#			-----  LOADING SCREENS  -----

@app.route('/gmodload')
def extra_gmodload(): 
	return flask.render_template('extra/loadscreen.html', game = 'gmod', a = a)

@app.route('/tf2motd')
def extra_tf2motd(): 
	return flask.render_template('extra/loadscreen.html', game = 'tf2', a = a)