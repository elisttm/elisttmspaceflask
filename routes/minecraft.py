from __main__ import app, flask, a, convert_plaintext
import urllib, urllib.request, json

# 		========================

def get_mcstats():
	return json.loads(urllib.request.urlopen(f"https://api.mcsrvstat.us/2/{urllib.parse.quote('mc.elisttm.space')}").read().decode('utf8'))

class mc():

	dynmap = "http://mc.elisttm.space:8123/"
	analytics = "http://mc.elisttm.space:8804/"
	recipes = ("elytra", "shulker", "saddle", "nametag", "leather",)
	
	rules = (
		"no cheating, hacking, griefing, stealing, rdm, etc",
		"respect the people playing on the server",
		"dont crash the server",
	)
	
	features = (
		"graves on death",
		"/spawn /tpa and /bed", 
		"custom recipes (see below)",
		"reliable backups (coreprotect)",
		"player analytics (plan)",
		"realtime map (dynmap)",
		"...and many more!" 
	)

# 		========================

@app.route('/minecraft')
def minecraft(): 
	return flask.render_template('minecraft.html', mcstats = get_mcstats(), mc = mc(), a = a)

@app.route('/minecraft/info')
def minecraft_info(): 
	mcstats = get_mcstats()
	mcstats_plugins = ''
	for plugin in mcstats['plugins']['names']:
		mcstats_plugins += f"- {plugin}\n"
	mc_info = f"mc.elisttm.space ({mcstats['ip']}:{mcstats['port']})\n\n{mcstats['version']} ({mcstats['software']})\n\nOnline: {mcstats['online']}\nPlayers: {mcstats['players']['online']}/{mcstats['players']['max']}\n\n{mcstats['motd']['clean'][0]}\n{mcstats['motd']['clean'][1]}\n\nPlugins:\n{mcstats_plugins}"
	mc_info_page = convert_plaintext(content = mc_info)
	return mc_info_page
