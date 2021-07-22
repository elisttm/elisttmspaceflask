import datetime
from datetime import datetime
import operator
import copy

class art():

	art_ = [

		# [image, timestamp, artist, artist-url, post-url]

		["amber.png", "March 23, 2021" , "amber", "https://twitter.com/minisodaparty"],
		["ambericon.png", "April 26, 2021", "amber", "https://twitter.com/minisodaparty"],
		["amberpride.png", "May 30, 2021", "amber", "https://twitter.com/minisodaparty"],
		["amberchibi.png", "June 3, 2021", "amber", "https://twitter.com/minisodaparty"],
		["amberpage.png", "June 9, 2021", "amber", "https://twitter.com/minisodaparty"],
		["ambermeow.png", "June 22, 2021", "amber", "https://twitter.com/minisodaparty"],

		["blake.png", "July 21, 2021", "blake", "https://twitter.com/cxtcvlt", "https://twitter.com/cxtcvlt/status/1417737900435849218"],

		["zesty1.png", "June 30, 2021", "zesty", "https://twitter.com/ZestyLemonss", "https://twitter.com/gecgender/status/1410327704654823428"],
		["zestyswag.png", "July 15, 2021", "zesty", "https://twitter.com/ZestyLemonss", "https://twitter.com/ZestyLemonss/status/1415719392546115584"],

		["witchfinder.png", "July 16, 2021", "witchfinder", "https://twitter.com/FINDEROFWITCHES", "https://twitter.com/FINDEROFWITCHES/status/1416084567581155332"],
		
		["nick.png", "June 16, 2021", "nick", "https://twitter.com/hearthurtzzz", "https://twitter.com/hearthurtzzz/status/1405374520266047490"],
		
		["exyli1.png", "July 3, 2021", "exyli", "https://twitter.com/exyli_", "https://twitter.com/Exyli_/status/1411300554098155537"],
		
		["goob.png", "May 28, 2021", "goob", "https://twitter.com/goobysart", "https://twitter.com/goobysart/status/1398454342957608964"],

		["miles.png", "March 25, 2021", "miles", "https://twitter.com/featherk1ss", "https://twitter.com/featherk1ss/status/1375110690776743936"],
		
		["milespride.png", "June 2, 2021", "miles", "https://twitter.com/featherk1ss", "https://twitter.com/featherk1ss/status/1400227222951239680"],
		
		["mileswatercolor.jpg", "June 15, 2021", "miles", "https://twitter.com/featherk1ss", "https://twitter.com/featherk1ss/status/1404882187250503681"],

		["churro.jpg", "March 12, 2021", "churro", "https://twitter.com/sockguts"],

		["teserex2.jpg", "June 8, 2021", "teserex", "https://twitter.com/teserex_exe", "https://twitter.com/teserex_exe/status/1402115848123342855"],
		
		["haikala.png", "June 20, 2021", "haikala", "https://twitter.com/sharkjpg", "https://twitter.com/sharkjpg/status/1406708741572018182"],

		["nabix.jpg", "April 6, 2021", "nabix", "https://twitter.com/Nabix_lol", "https://twitter.com/Nabix_lol/status/1379524309648089089"],

		["azereii.png", "June 22, 2021", "azereii", "https://twitter.com/azereii", "https://twitter.com/azereii/status/1407415818158288899"],
		
		["shermy1.png", "July 12, 2021", "sherm", "https://twitter.com/shermtwt", "https://twitter.com/shermtwt/status/1414666966955171840"],
		["shermchoke.png", "July 22, 2021", "sherm", "https://twitter.com/shermtwt", "https://twitter.com/shermtwt/status/1418305585137819650"],

		["glowy.jpg", "April 13, 2021", "glowy", "https://twitter.com/glowyart", "https://twitter.com/glowyart/status/1382013628640075776"],
		
		["doe.jpg", "May 27, 2021", "doe", "https://twitter.com/doeblush"],
		
		["popbob.jpg", "March 22, 2021", "popbob", "https://twitter.com/P0pbob", "https://twitter.com/P0pbob/status/1373947896245129217"],
		
		["mora.jpg", "February 25, 2021", "mora", "https://twitter.com/moragilerto"],
		
		["josh.jpg", "November 19, 2020", "josh", "https://twitter.com/cumttv"],
		
		["maureendamn.jpg", "May 17, 2021", "llamasaur", "https://twitter.com/haz_a_biscuit"],

		["llamagay.png", "January 16, 2021", "llamasaur", "https://twitter.com/haz_a_biscuit"],
		
		["faefuck.png", "November 12, 2020", "fae", "https://twitter.com/AlexisDebroux"],
				
		["darekit.png", "March 30, 2021", "boots", "https://twitter.com/darekit", "https://twitter.com/darekit/status/1377070470902714377"],

		["bennsect.png", "July 7, 2021", "bennsect", "https://artfight.net/~bennsect", "https://artfight.net/attack/2116796.eli"],

		["max.png", "February 22, 2021", "max", "https://twitter.com/yeen_fiend"],

		["satty.png", "May 9, 2021", "satty", "https://twitter.com/sadsatty", "https://twitter.com/sadsatty/status/1391470688104505348"],
		
		["grant.jpg", "November 23, 2020", "grant"],
		
		["devburger.png", "October 11, 2020", "dev"],
		
		["sam.png", "October 6, 2020", "sam"],
		
		["samstfu.jpg", "December 9, 2020", "sam"],
		
		["nikkivrc.png", "March 11, 2021", "nikki", "https://twitter.com/fiishfin", "https://twitter.com/fiishfin/status/1370219104125255681"],
		
		["grumm2b.jpg", "October 7, 2020", "grumm", "https://twitter.com/grummBB"],
		["grumm3c.png", "December 7, 2020", "grumm", "https://twitter.com/grummBB"],
		
		["skedgymeow.png", "May 25, 2021", "skedgy", "https://twitter.com/skedgyedgy"],
		["skedgymurder.png", "February 15, 2021", "skedgy", "https://twitter.com/skedgyedgy"],
				
		["fluffer.png", "July 20, 2020", "fluffer", "https://twitter.com/sofluffer"],
		
		["smeefaroni.jpg", "February 28, 2021", "smeefaroni", "https://twitter.com/smeefaroni", "https://twitter.com/smeefaroni/status/1366143272029204482"],

		["sharpzbday.png", "February 10, 2021", "sharpz", "https://twitter.com/_Sharpz", "https://twitter.com/Sharpz_Art/status/1359559872921153539"],

		["calvin1.png", "November 1, 2020", "calvin", "https://twitter.com/sic_trix"],
		
		["calvin.png", "December 10, 2020", "calvin", "https://twitter.com/sic_trix"],
		
		["skyaninsane.png", "October 7, 2020", "skyan", "https://twitter.com/SkyanUltra"],

		["origay.png", "January 1, 2021", "ori", "https://twitter.com/audio_ori"],
		["origay2.png", "January 7, 2021", "ori", "https://twitter.com/audio_ori"],
		["orikitten.png", "February 2, 2021", "ori", "https://twitter.com/audio_ori"],
		
	]

	sorted_art = copy.deepcopy(art_)
	for piece in sorted_art:
		piece[1] = datetime.strptime(piece[1], '%B %d, %Y')
	sorted_art = sorted(sorted_art, key=operator.itemgetter(1), reverse=True)
	for piece in sorted_art:
		piece[1] = datetime.strftime(piece[1], '%B %d, %Y')