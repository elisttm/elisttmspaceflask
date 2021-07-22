from __main__ import app, flask, a

# 		========================

class indx():
	
	keywords = "elisttm, elisttm2, elittm, eli, trashbot, mc.elisttm.space"

	sm_buttons = {
		'twitter': a.twitter,
		'youtube': a.youtube,
		'steam': a.steam,
		'github': a.github,
		#'discord': a.discord,
	}

	buttons = {
		"/eli": {"a": "my fursona", "b": "my fursonas ref + gallery"},
		"/trashbot": {"a": "trashbot", "b": "my discord bot"},
		"/minecraft": {"a": "mc.elisttm.space", "b": "my minecraft server"},
		"/pack": {"a": "eli pack", "b": "my resource pack"},
		"/cats": {"a": "random cats", "b": "my funny cat website"},
		"https://twitter.com/i/events/1377729588709703683": {"a": "my art", "b": "all in one twitter moment"}
	}

	info = (
		"hi! im eli, im a 16 year old programmer artist computer nerd cat person and this is my website!",
		"this site is somewhat regularly updated and currently contains many pages of projects ive worked on!",
		"you can find links to my social media/contacts and other pages on and off this site below!",
		"if you find a bug or have a suggestion for the website, feel free to contact me.",
	)

# 		========================

@app.route('/')
def index(): 
	return flask.render_template('index.html', indx = indx(), a = a, )
