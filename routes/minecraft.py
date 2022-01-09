from __main__ import app, flask, a
import urllib, urllib.request, json

def get_mcstats(): 
	return json.loads(urllib.request.urlopen(f"https://api.mcsrvstat.us/2/{urllib.parse.quote('mc.elisttm.space')}").read().decode('utf8'))

class mc():

	dynmap = "http://mc.elisttm.space:8123/"
	stats = "http://mc.elisttm.space:8804/server/elisttm"
	old_worlds = "https://www.mediafire.com/folder/12kozz7hn0olx/mcserver"
	
	recipedir = f'{a.img}recipes/'
	recipes = ("elytra", "shulker", "saddle", "nametag", "leather",)

	buttons = (
		(dynmap, 'dynmap'),
		(stats, 'player stats'),
		(old_worlds, 'world archives'),
	)

	rules = (
		"no cheating, griefing, stealing, etc",
		"respect the people playing on the server",
		"dont crash the server",
	)
	
	features = (
		"graves on death",
		"/spawn /tpa and /home", 
		"realtime world map",
		"reliable logging and rollbacks",
		"supports joining on bedrock and most java versions",
		"custom recipes", 
	)

#@app.route('/minecraft')
#def minecraft(): 
#	return flask.render_template('minecraft.html', mc = mc(), a = a)
#
#@app.route('/minecraft/upcheck')
#def upcheck(): 
#	text = 'the server is currently offline'
#	if get_mcstats()['online'] == True:
#		text = 'the server is currently online'
#	return f'<link rel="stylesheet" href="{a.css}" type="text/css"/><body class="content"><p align="center">{text}</p></body>' 
