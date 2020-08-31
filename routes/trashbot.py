from __main__ import app, flask, a

# 		========================

class tb():
	
	invite = "https://discordapp.com/oauth2/authorize?client_id=439166087498825728&scope=bot&permissions=8"
	github = "https://github.com/elisttm/trashbot"
	cmds = "https://trashbot.elisttm.space/commands"
	tags = "https://trashbot.elisttm.space/tags"

	features = (
		"commands using a growing database of cat pictures", 
		"utility commands for server/user info", 
		"customizable prefix per server",
		"active support and updates", 
		"reliable and high uptime",
		"tag database command",
		"...and more!", 
	)

# 		========================

@app.route('/trashbot')
def trashbot(): 
	return flask.render_template('trashbot.html', tb = tb(), a = a)
