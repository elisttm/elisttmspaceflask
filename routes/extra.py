from __main__ import app, flask, a

	# =====  error handlers  =====

errors = {
	'403': ["403: access is denied","you are not authorized to access this page!"],
	'404': ["404: page could not be found", "the url you entered could not be found.",],
	'500': ["500: internal server error", "the requested page caused an error and could not be loaded.",]
}

@app.errorhandler(403)
def forbidden(error): 
	return flask.render_template('extra/errors.html', e = '403', no_analytics = True, errors = errors, a = a), 403

@app.errorhandler(404)
def page_not_found(error): 
	return flask.render_template('extra/errors.html', e = '404', no_analytics = True, errors = errors, a = a), 404

@app.errorhandler(500)
def internal_server(error): 
	return flask.render_template('extra/errors.html', e = '500', no_analytics = True, errors = errors, a = a), 500

	# =====  source load screens  =====

@app.route('/gmodload')
def extra_gmodload(): 
	return flask.render_template('extra/loadscreen.html', game = 'gmod', a = a)

@app.route('/tf2motd')
def extra_tf2motd(): 
	return flask.render_template('extra/loadscreen.html', game = 'tf2', a = a)
