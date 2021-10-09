from __main__ import app, flask, a

class tb():
	
	invite = "https://discord.com/api/oauth2/authorize?client_id=439166087498825728&scope=bot&permissions=1544416321"
	github = "https://github.com/elisttm/trashbot"
	cmds = "https://trashbot.elisttm.space/commands"
	tags = "https://trashbot.elisttm.space/tags"

	buttons = (
		(invite, 'bot invite'),
		(cmds, 'commands'),
		(github, 'source code'),
	)

	features = ( 
		"informative utility commands",
		"fully customizable starboard", 
		"join/leave messages, autorole, and stickyroles", 
		"dashboard webpage for configuration",
		"reliable uptime",
		"...and more!", 
	)

	planned = (
		"reaction roles",
		"reminders?",
		"changelog",
	)

@app.route('/trashbot')
def trashbot(): 
	return flask.render_template('trashbot.html', tb = tb(), a = a)
