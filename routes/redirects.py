from __main__ import app, flask, a

# 		========================

rhcrules = "https://docs.google.com/document/d/1PwdC3RJW-puAVBJ7mxIGrKKObLdAApvalQPmPYduv18"
gmodsrv = "steam://connect/play.elisttm.space/chungus"

# 		========================

@app.route('/gmodsrv')
def redirect_gmod(): 
	return flask.render_template('redirects/gmodsrv.html', gmodsrv = gmodsrv, a = a)

@app.route('/rhc')
def redirect_rhc(): 
	return flask.render_template('redirects/rhc.html', rhcrules = rhcrules, a = a)
	