from __main__ import app, flask, a

# 		========================

class mcpk():

	version = "1.6"
	download = "https://www.mediafire.com/file/y97fmg8ebt24niu/eli_pack_%255Bv1.6%255D.zip/file"
	legacydownload = "https://www.mediafire.com/file/a2kxearuwrgp33c/eli_pack_%2528legacy%2529_%255Bv1.6%255D.zip/file"
	
pack_changelog = {
	'2021': {
		"v1.6 - ":"(6/30) seperated the 1.8 pack from the 1.17 pack; updated textures for 1.17, added some 1.17 textures, and updated some older textures",
		"v1.5 - ":"(6/18) added @trickmynt's rainbow ancient debris textures, altered a bunch of textures for consistency, and added several vanillatweaks packs (i dont remember specifically which ones)",
		"v1.4 - ":"(2/26) rebranded to \"eli pack\"; added netherite armor textures and altered many other textures for consistency",
	},
	'2020': {
		"v1.3 - ":"(7/19) minor updates to ui textures introduced in 1.16",
		"v1.2.1 - ":"(6/16) changed the wither skeleton texture to be more consistent with the regular skeleton texture",
		"v1.2 - ":"(6/15) removed repetitive and unchanged files and compressed some others to reduce overall filesize of both packs (22mb -> 5mb)",
		"v1.1 - ":"(2/15) updated guis for both packs; also added a link to here in the pack description",
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
