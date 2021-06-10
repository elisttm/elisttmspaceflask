from __main__ import app, flask, a

# 		========================

gmodsrv = "steam://connect/play.elisttm.space/chungus"

okyeah = {
	"discord": a.discord,
}

# 		========================

@app.route('/gmodsrv')
def redirect_gmod(): 
	return flask.render_template('redirects/gmodsrv.html', gmodsrv = gmodsrv, a = a)
