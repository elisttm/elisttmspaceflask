from __main__ import app, flask, a, get_mcstats

# 		========================

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
	mcstats = get_mcstats()
	return flask.render_template('index.html', mcstats = mcstats, sm_buttons = sm_buttons, a = a, )
