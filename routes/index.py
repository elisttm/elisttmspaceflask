from __main__ import app, flask, a

# 		========================

class indx():

	keywords = "elisttm, elijahsttm, elijah the trash man, creeperstorm75, trashbot"

	sm_buttons = {
		'twitter': a.twitter,
		'youtube': a.youtube,
		'steam': a.steam,
		'github': a.github,
		'discord': a.discord,
		'patreon': a.patreon,
	}

	sections = {
		'trashbot': {
			'desc': 'a simple discord.py bot with various features',
			'path': ['/trashbot'],
			'hr': 60
		},
		'minecraft server': {
			'desc': 'a 1.16.2 vanilla smp server that i host, manage and develop',
			'path': ['/minecraft'],
			'hr': 60
		},
		'my website': {
			'desc': 'a flask backended website that i develop (hint: its this one)',
			'path': ['/website'],
			'hr': 60
		},
		'random cats': {
			'desc': 'a personally hosted page that serves random cat pictures from my personal collection of funny cats',
			'path': ['/cats'],
			'hr': 60
		},
		'gmod server': {
			'desc': 'a pretty cool garrys mod server that i host and manage',
			'path': ['/gmod'],
			'hr': 60
		},
		'eli\'s cool resource pack': {
			'desc': 'my personal minecraft resource pack for 1.8x and 1.14+',
			'path': ['/pack'],
			'hr': 75
		},
	}

# 		========================

@app.route('/')
def index(): 
	return flask.render_template('index.html', indx = indx(), a = a, )
