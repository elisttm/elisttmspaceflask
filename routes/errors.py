from __main__ import app, flask, a

# 		========================

@app.errorhandler(403)
def forbidden(error):
	return flask.render_template('errors.html', no_analytics = True, error = error, error_name = "403 forbidden", a = a), 403

@app.errorhandler(404)
def page_not_found(error):
	return flask.render_template('errors.html', no_analytics = True, error = error, error_name = "404 not found", a = a), 404

@app.errorhandler(500)
def internal_server(error):
	return flask.render_template('errors.html', no_analytics = True, error = error, error_name = "500 internal server error", a = a), 500
