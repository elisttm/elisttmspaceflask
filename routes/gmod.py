from __main__ import app, flask, a

# 		========================

class gm():

	redirect = "steam://connect/play.elisttm.space/chungus"

	rules = (
		"respect the people playing on the server",
		"dont crash the server",
	)
	
	collections = {
		"sandbox addons": "https://steamcommunity.com/sharedfiles/filedetails/?id=2084328429",
		"gamemode addons": "https://steamcommunity.com/sharedfiles/filedetails/?id=2085165984",
		"relevant maps": "https://steamcommunity.com/sharedfiles/filedetails/?id=2169587352",
	}

# 		========================

@app.route('/gmod')
def gmod(): 
	return flask.render_template('gmod.html', gm = gm(), a = a)
