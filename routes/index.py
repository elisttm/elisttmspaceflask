from __main__ import app, flask, a, get_mcstats

# 		========================

keywords = "elisttm, elijahsttm, elijah the trash man, creeperstorm75, trashbot"

sm_buttons = {
	'twitter': a.twitter,
	'youtube': a.youtube,
	'steam': a.steam,
	'github': a.github,
	'discord': a.discord,
	'patreon': a.patreon,
}

# 		========================

@app.route('/')
def index(): 
	print("elisttm.space" + flask.request.path)
	return flask.render_template('index.html', sm_buttons = sm_buttons, a = a, )
