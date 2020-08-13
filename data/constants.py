class constants():

	css = "/static/style.css"
	js = "/static/script.js"
	logo = "/static/logo.png"
	favicon = "/static/favicon.ico"

	images = "/static/images"
	logos = "/static/images/logos"

	twitter = "https://twitter.com/elisttm"
	youtube = "https://www.youtube.com/c/elisttm"
	steam = "https://steamcommunity.com/id/elisttm"
	github = "https://github.com/elisttm"
	discord = "https://discord.com/invite/a9UUJ3P"
	patreon = "https://www.patreon.com/elisttm"
	paypal = "https://paypal.me/thetrashman"

	rickroll = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"


	mc_version = '1.16.2'
	mc_dynmap = 'http://mc.elisttm.space:8123/'
	mc_analytics = 'http://mc.elisttm.space:8804/'

	trashbot_invite = 'https://discordapp.com/oauth2/authorize?client_id=439166087498825728&scope=bot&permissions=8'
	trashbot_github = 'https://github.com/elisttm/trashbot'
	trashbot_cmds = 'https://trashbot.elisttm.repl.co'

	pack_version = '1.3.0'
	pack_base = "https://www.mediafire.com/file/z0rbmyf9wrf56ew/eli%27s_epic_gamer_pack_%5Bv1.3.0%5D.zip/file"
	pack_overlay = "https://www.mediafire.com/file/p2157v1ved7c2cb/eli%27s_epic_gamer_pack_1.14+_overlay.zip/file"

	website_github = 'https://github.com/elisttm/elisttmspaceflask'

	gmodsrv = "steam://connect/play.elisttm.space/chungus"
	rhcrules = "https://docs.google.com/document/d/1PwdC3RJW-puAVBJ7mxIGrKKObLdAApvalQPmPYduv18"


	t_prefix = ""
	t_suffix = " | elisttm"

	keywords = "elisttm, elijahsttm, elijah the trash man, creeperstorm"


	pages = [
		"https://elisttm.space/",
		"https://elisttm.space/sitemap",
		"https://elisttm.space/minecraft",
		"https://elisttm.space/trashbot",
		"https://elisttm.space/pack",
		"https://elisttm.space/donors",
		"https://elisttm.space/style",
		"https://elisttm.space/sitemap.xml",
		"https://elisttm.space/robots.txt",
	]

	donor_list = [
		"($10) Tao Scree", 
		"($2) SoFluffer"
	]

	mc_rules = [
		"no cheating, hacking, griefing, stealing, rdm, etc",
		"respect the people playing on the server",
		"dont crash the server",
	]

	mc_features = [
		"/spawn and /tpa", 
		"graves on death",
		"custom recipes/datapacks",
		"reliable backups (coreprotect)",
		"enhanced sleeping (harbor)", 
		"realtime map (dynmap)", 
	]

	trashbot_features = [
		"commands using a growing database of cat pictures", 
		"utility commands for server/user info", 
		"active support and updates", 
		"reliable and high uptime",
		"...and more!", 
	]

	pack_features = [
		"gonna update this list later",
	]



class pack_changelog():

	_2020 = {
			"v1.3.0 - ":"(7/19) minor updates to ui textures introduced in 1.16",
			"v1.2.1 - ":"(6/16) changed the wither skeleton texture to be more consistent with the regular skeleton texture",
			"v1.2.0 - ":"(6/15) removed repetitive and unchanged files and compressed some others to reduce overall filesize of both packs (22mb -> 5mb)",
			"v1.1.0 - ":"(2/15) updated guis for both packs; also added a link to here in the pack description",
	}
	_2019 = {
			"v1.0.1 - ":"(10/14) Changed icons and descriptions of both packs to better reflect this page",
			"v1.0.0 - ":"(10/8) Created the resource pack page (public pack release)",		
	}
	historical = {
			"pre1.0 - ":"(late 2018) Renamed PvP overlay to \"eli\'s epic gamer pack\" and transferred any good aspects of previous packs to it",
			"pre0.2 - ":"(late 2017) Transferred practical aspects of the meme pack to a 1.8 PvP overlay pack",
			"pre0.1 - ":"(early 2017) Created \"elijah\'s meme pack\" which was basically this pack but less practical",
	}

	changelogs = {"2020": _2020, "2019": _2019, "Historical Versions (before 2018)": historical,}

	changelog_page = """<style>p {color:#fff;font-family:monospace;text-align:justify;line-height:1.25;padding: 0 25px 0 25px;} h4 {color: #fff;font-family:monospace;text-align:center;}</style><p>"""

	for x, y in changelogs.items():
		changelog_page = changelog_page + f"</p><h4>{x}</h4><br><p>"
		yy = dict(y)
		for a, b in yy.items():
			changelog_page = changelog_page + f"<b>{a}</b>{b}<br><br>"