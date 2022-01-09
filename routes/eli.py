import os, operator, copy
from __main__ import app, flask, a
from datetime import datetime
from PIL import Image

class eliart:
	_art_ = [
	# [filename 					YY-MM-DD		artist				link to artist, link to post]
		["amber.png",				"21-03-23",	"amber",			"https://twitter.com/minisodaparty"],
		["amberchibi.jpg",	"21-06-03",	"amber",			"https://twitter.com/minisodaparty"],
		["amberpage.png",		"21-06-19",	"amber",			"https://twitter.com/minisodaparty"],
		["ambermeow.png",		"21-06-22",	"amber",			"https://twitter.com/minisodaparty"],
		["amberGAY.png",		"21-08-05",	"amber",			"https://twitter.com/minisodaparty", "https://twitter.com/i/status/1424437626149429250"],
		["milespride.png",	"21-06-02",	"miles",			"https://twitter.com/featherk1ss", "https://twitter.com/i/status/1400227222951239680"],
		["mileswc.jpg",			"21-06-15",	"miles",			"https://twitter.com/featherk1ss", "https://twitter.com/i/status/1404882187250503681"],
		["milespainting.png","21-12-09","miles",			"https://twitter.com/featherk1ss"],
		["blake.png",				"21-07-21",	"blake",			"https://twitter.com/cxtcvlt",	"https://twitter.com/i/status/1417737900435849218"],
		["blakepage.png",		"21-10-19",	"blake",			"https://twitter.com/cxtcvlt",	"https://twitter.com/cxtcvlt/status/1450597148324769795"],
		["zesty1.png",			"21-06-30",	"zesty",			"https://twitter.com/ZestyLemonss", "https://twitter.com/i/status/1410327704654823428"],
		["zestyswag.png",		"21-07-15",	"zesty",			"https://twitter.com/ZestyLemonss", "https://twitter.com/i/status/1415719392546115584"],
		["nick.png",				"21-06-16",	"nick",				"https://twitter.com/hearthurtzzz", "https://twitter.com/i/status/1405374520266047490"],
		["nicklaptop.png",	"21-08-04",	"nick",				"https://twitter.com/hearthurtzzz", "https://twitter.com/i/status/1423034202451238916"],
		["nickhoodie.png",	"21-09-03",	"nick",				"https://twitter.com/hearthurtzzz", "https://twitter.com/i/status/1433745703990353948"],
		["nickclothes.png",	"21-09-13",	"nick",				"https://twitter.com/hearthurtzzz", "https://twitter.com/i/status/1437605962811072513"],
		["mars.png",				"21-07-10",	"mars",				"https://twitter.com/marz_rom_", "https://twitter.com/i/status/1413755342127779841"],
		["marssillay.png",	"21-08-20",	"mars",				"https://twitter.com/marz_rom_", "https://twitter.com/i/status/1428582497517023239"],
		["marshardasf.png",	"21-08-22",	"mars",				"https://twitter.com/marz_rom_", "https://twitter.com/i/status/1429635720709345280"],
		["morgmorg.png",		"21-08-26",	"morg",				"https://twitter.com/killsmorg", "https://twitter.com/i/status/1431004190516596743"],
		["morgcomm.png",		"21-09-02",	"morg",				"https://twitter.com/killsmorg"],
		["zeeswag.png",			"21-08-31",	"zee",				"https://twitter.com/zmag2288", "https://twitter.com/i/status/1432556428066058242"],
		["t3rror.png",			"21-07-29",	"t3rror",			"https://twitter.com/T3rrorc0n", "https://twitter.com/i/status/1420855374156992513"],
		["witchfinder.png",	"21-07-16",	"witchfinder","https://twitter.com/FINDEROFWITCHES", "https://twitter.com/i/status/1416084567581155332"],
		["jaden.png",				"21-07-29",	"jaden",			"https://twitter.com/fennykinz", "https://twitter.com/i/status/1420752136061603842"],
		["exyli1.png",			"21-07-03",	"exyli",			"https://twitter.com/exyli_", "https://twitter.com/i/status/1411300554098155537"],
		["sthom.png",				"21-08-14",	"sthom",			"https://twitter.com/sthomtj", "https://twitter.com/i/status/1426609775010271233"],
		["goob.png",				"21-05-28",	"goob",				"https://twitter.com/goobysart", "https://twitter.com/i/status/1398454342957608964"] ,
		["azereii.png",			"21-06-22",	"azereii",		"https://twitter.com/azereii", "https://twitter.com/i/status/1407415818158288899"],
		["shermchoke.png",	"21-07-22",	"sherm",			"https://twitter.com/shermtwt", "https://twitter.com/i/status/1418305585137819650"],
		["shermcray.png",		"21-08-22",	"sherm",			"https://twitter.com/shermtwt", "https://twitter.com/i/status/1427088757342326786"],
		["glowy.jpg",				"21-04-13",	"glowy",			"https://twitter.com/glowyart", "https://twitter.com/i/status/1382013628640075776"],
		["doe.jpg",					"21-05-27",	"doe", 				"https://twitter.com/doeblush"],
		["maureendamn.jpg",	"21-05-17",	"llamasaur",	"https://twitter.com/haz_a_biscuit"],
	]

	data_timeformat = '%y-%m-%d' 			# YY-MM-DD
	cosmetic_timeformat = '%B %d, %Y' # January 1, 2000

	art = copy.deepcopy(_art_)
	art_time = sorted(copy.deepcopy(_art_), key=operator.itemgetter(1), reverse=True)

	path = a.img[1:]+'eli/gallery/'
	cpath = path+'yeah/'

	for piece in art: piece[1] = datetime.strftime(datetime.strptime(piece[1], data_timeformat), cosmetic_timeformat)
	for piece in art_time: piece[1] = datetime.strftime(datetime.strptime(piece[1], data_timeformat), cosmetic_timeformat)

	for piece in _art_: 
		filename = piece[0].replace('.png','.jpg')
		if 'COMPRESSED_'+filename not in os.listdir(cpath):
			img = Image.open(path+piece[0])
			if img.mode in ("RGBA","P"): img=img.convert('RGB')
			img.save(cpath+'COMPRESSED_'+filename, optimize=True, quality=50); print(f'compressed {filename}')

class eli:

	dir = a.img+'eli/'

	a.sitemap_stuff[1][2] = '2021-07-31'; a.sitemap_stuff[2][2] = '2021-12-09'
	lastupdate_ref = datetime.strftime(datetime.strptime(a.sitemap_stuff[1][2], a.sitemap_timeformat), eliart.cosmetic_timeformat)
	lastupdate_art = datetime.strftime(datetime.strptime(a.sitemap_stuff[2][2], a.sitemap_timeformat), eliart.cosmetic_timeformat)

	info = (
		"funny cat",
		"gremlin shaped entity of chaos",
		"clothes and accessories are fine",
	)

@app.route('/eli')
def fursona(): 
	return flask.render_template('eli.html', eli = eli, a = a)

sorting = {
	None: eliart.art, 
	'new': eliart.art_time,
}

@app.route('/eli/art', defaults={'s': None})
def eli_art(s):
	if flask.request.args:
		s = flask.request.args['s'] if not s else s
		if not s: 
			flask.abort(404)
	return flask.render_template('eliart.html', art=sorting[s], eliart=eliart, sort=s, eli=eli, a=a)
