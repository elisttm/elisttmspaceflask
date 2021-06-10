from __main__ import app, flask, a

# 		========================

class mcpk():

	version = "1.4.0"
	base = "http://www.mediafire.com/file/reoj4nha9trr68e/eli_pack_%255Bv1.4.0%255D.zip/file"
	overlay = "http://www.mediafire.com/file/fqcv29udxt0gtr0/eli_pack_1.16%252B_overlay.zip/file"
	
	features = (
		"natural blocks are softer and nicer to look at",
		"less intrusive food and shield viewmodels",
		"replaced sounds with more pleasant versions",
		"...and more! (too lazy to list them)",
	)

pack_changelog = {
	'2021': {
		"v1.4.0 - ":"(2/26) renamed to \"eli pack\"; added netherite armor textures aswell as altered and cut down on many many other textures",
	},
	'2020': {
		"v1.3.0 - ":"(7/19) minor updates to ui textures introduced in 1.16",
		"v1.2.1 - ":"(6/16) changed the wither skeleton texture to be more consistent with the regular skeleton texture",
		"v1.2.0 - ":"(6/15) removed repetitive and unchanged files and compressed some others to reduce overall filesize of both packs (22mb -> 5mb)",
		"v1.1.0 - ":"(2/15) updated guis for both packs; also added a link to here in the pack description",
	},
	'2019': {
		"v1.0.1 - ":"(10/14) Changed icons and descriptions of both packs to better reflect this page",
		"v1.0.0 - ":"(10/8) Created the resource pack page (public pack release)",		
	},
	'Historical Versions (before 2018)': {
		"pre1.0 - ":"(late 2018) Renamed PvP overlay to \"eli\'s epic gamer pack\" and transferred any good aspects of previous packs to it",
		"pre0.2 - ":"(late 2017) Transferred practical aspects of the meme pack to a 1.8 PvP overlay pack",
		"pre0.1 - ":"(early 2017) Created \"elijah\'s meme pack\" which was basically this pack but less practical",
	}
}

# 		========================

@app.route('/pack')
def pack(): 
	return flask.render_template('pack.html', mcpk = mcpk(), a = a)

@app.route('/pack/changelog')
def pack_changelogs(): 
	changelog_page = "<style>p {color:#fff;font-family:monospace;text-align:justify;line-height:1.25;padding: 0 25px 0 25px;} h4 {color: #fff;font-family:monospace;text-align:center;}</style><p>"
	for year in pack_changelog:
		changelog_page += f"<p><h4>{year}</h4><br><p>"
		for version, changes in pack_changelog[year].items():
			changelog_page += f"<b>{version}</b>{changes}<br><br>"
	return changelog_page
