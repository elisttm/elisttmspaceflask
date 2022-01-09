from __main__ import app, flask, a

class indx():
	
	keywords = "elisttm, elisttm2, elittm, eli, trashbot, mc.elisttm.space"

	icon_dir = f'{a.img}/logos/'
	sm_buttons = (
		('twitter', a.twitter),
		('youtube', a.youtube),
		('steam', a.steam),
		('github', a.github),
		#('discord', a.discord),
	)

	buttons = (
		("/eli", "my fursona", "my sonas ref + art gallery"),
		("/trashbot", "trashbot", "my discord bot"),
		("/minecraft", "mc.elisttm.space", "my minecraft server"),
		("/pack", "eli pack", "my resource pack"),
		#("http://e.elisttm.space:7777/", "random cats", "my funny cat website"),
		("https://twitter.com/i/events/1377729588709703683", "my art", "all in one twitter moment")
	)

	info = (
		"hi! im eli, im a 16 year old programmer artist computer nerd cat person and this is my website!",
		"this site is somewhat regularly updated and currently contains many pages of projects ive worked on!",
		"you can find links to my social media/contacts and other pages on and off this site below!",
		"NOTE: the site is being updated soon and some pages have intentionally been disabled",
	)

@app.route('/')
def index(): 
	return flask.render_template('index.html', indx = indx(), a = a, )
