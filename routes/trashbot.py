from __main__ import app, flask, a
import urllib, urllib.request, json

# 		========================

class tb():
	
	invite = "https://discordapp.com/oauth2/authorize?client_id=439166087498825728&scope=bot&permissions=8"
	github = "https://github.com/elisttm/trashbot"
	cmds = "http://e.elisttm.space:42069/"
	tags = "http://e.elisttm.space:42069/tags"

	features = ( 
		"utility commands for useful information",
		"customizable join/leave messages, autorole and stickyroles", 
		"customizable starboard", 
		"reliable + high uptime",
		"global tag database",
		"funny cat commands",
		"...and more!", 
	)

	planned = (
		"higher degree of per-server customization",
		"settings dashboard website",
		"reaction role menu creator and editor",
	)

# 		========================

@app.route('/trashbot')
def trashbot(): 
	return flask.render_template('trashbot.html', tb = tb(), a = a)