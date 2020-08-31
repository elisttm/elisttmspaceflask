from __main__ import app, flask, a

# 		========================

rhcrules = "https://docs.google.com/document/d/1PwdC3RJW-puAVBJ7mxIGrKKObLdAApvalQPmPYduv18"

# 		========================

@app.route('/gmodsrv')
def redirect_gmod(): 
	return flask.render_template('redirects/gmodsrv.html', gmodsrv = a.gmod_redirect, a = a)

@app.route('/rhc')
def redirect_rhc(): 
	return flask.render_template('redirects/rhc.html', rhcrules = rhcrules, a = a)
	