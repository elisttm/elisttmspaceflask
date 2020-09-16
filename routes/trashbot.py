from __main__ import app, flask, a
import urllib, urllib.request, json

# 		========================

class tb():
	
	invite = "https://discordapp.com/oauth2/authorize?client_id=439166087498825728&scope=bot&permissions=8"
	github = "https://github.com/elisttm/trashbot"
	cmds = "https://trashbot.elisttm.space/commands"
	tags = "https://trashbot.elisttm.space/tags"

	features = ( 
		"utility commands for useful information", 
		"customizable prefix per server",
		"active support and updates", 
		"reliable + high uptime",
		"global tag database",
		"random cat commands",
		"...and more!", 
	)

	planned = (
		"highly customizable per-server settings",
		"more user suggested commands",
		"settings dashboard website",
	)

# 		========================

@app.route('/trashbot')
def trashbot(): 
	return flask.render_template('trashbot.html', tb = tb(), a = a)
