from __main__ import app, flask, a

# 		========================

@app.route('/sitemap')
def sitemap(): 
	return flask.render_template('sitemap.html', a = a)

@app.route('/styles')
def style(): 
	return flask.render_template('style.html', a = a)

@app.route('/funny')
def funny(): 
	funnyarg = flask.request.args.get('f')
	return flask.render_template('extra/funny.html', funnyarg = funnyarg, a = a)

@app.route('/gmodload')
def extra_gmodload(): 
	return flask.render_template('extra/gmodload.html', a = a)

@app.route('/tf2motd')
def extra_tf2motd(): 
	return flask.render_template('extra/tf2motd.html', a = a)