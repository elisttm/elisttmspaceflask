from __main__ import app, flask, a, convert_plaintext
import urllib, urllib.request, json

# 		========================

def get_mcstats():
	return json.loads(urllib.request.urlopen(f"https://api.mcsrvstat.us/2/{urllib.parse.quote('mc.elisttm.space')}").read().decode('utf8'))

class mc():

	dynmap = "http://mc.elisttm.space:8123/"
	plan = "http://mc.elisttm.space:8804/server/elisttm"
	recipes = ("elytra", "shulker", "saddle", "nametag", "leather",)
	old_worlds = "https://www.mediafire.com/folder/12kozz7hn0olx/mcserver"
	
	rules = (
		"no cheating, griefing, stealing, etc",
		"respect the people playing on the server",
		"dont crash the server",
	)
	
	features = (
		"graves on death",
		"/spawn /tpa and /home", 
		"support for bedrock accounts",
		"reliable backups (coreprotect)",
		"realtime world map (dynmap)",
		"custom recipes (see below)",
		"...and many more!" 
	)

# 		========================

@app.route('/minecraft')
def minecraft(): 
	return flask.render_template('minecraft.html', mcstats = get_mcstats(), mc = mc(), a = a)

@app.route('/minecraft/recipes')
def recipes(): 
	return flask.render_template('extra/recipes.html', mc = mc(), a = a)

@app.route('/minecraft/upcheck')
def upcheck(): 
	mcstats = get_mcstats()
	if mcstats['online'] == True:
		return f'<link rel="stylesheet" href="{a.css}" type="text/css" /><body class="content"><p align="center">the server is currently online!</p></body>'
	else:
		return f'<link rel="stylesheet" href="{a.css}" type="text/css" /><body class="content"><p align="center">the server is currently offline</p></body>'
	return 



#@app.route('/minecraft/info')
#def minecraft_info(): 
#	mcstats = get_mcstats()
#	mcstats_plugins = ''
#	for plugin in mcstats['plugins']['names']:
#		mcstats_plugins += f"- {plugin}\n"
#	mc_info = f"mc.elisttm.space ({mcstats['ip']}:{mcstats['port']})\n\n{mcstats['version']} ({mcstats['software']})\n\nOnline: {mcstats['online']}\nPlayers: {mcstats['players']['online']}/{mcstats['players']['max']}\n\n{mcstats['motd']['clean'][0]}\n{mcstats['motd']['clean'][1]}\n\nPlugins:\n{mcstats_plugins}"
#	mc_info_page = convert_plaintext(content = mc_info)
#	return mc_info_page
