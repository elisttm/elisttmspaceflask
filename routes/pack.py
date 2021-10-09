from __main__ import app, flask, a

class mcpk():

	version = "1.6.1"
	download = "https://www.mediafire.com/file/1jtqfjnlhor1k69/eli_pack_%255Bv1.6.1%255D.zip/file"
	legacydownload = "https://www.mediafire.com/file/brnf10rpab8dthr/eli_pack_%2528legacy%2529_%255Bv1.6.1%255D.zip/file"
	
changelog = {
	'2021': [
		["1.6.1", "7/22", "fixed a bunch of mistakes i accidentally made after the last update"],
		["1.6", "6/30", "seperated the 1.8 pack from the 1.17 pack; updated textures for 1.17, added some 1.17 textures, and updated some older textures"],
		["1.5", "6/18", " added @trickmynt's rainbow ancient debris textures, altered a bunch of textures for consistency, and added several newer vanillatweaks features"],
		["1.4", "2/26", "rebranded to \"eli pack\"; added netherite armor textures and altered many other textures for consistency"],
	],
	'2020': [
		["1.3", "7/19", "minor updates to ui textures introduced in 1.16"],
		["1.2.1", "6/16", "changed the wither skeleton texture to be more consistent with the regular skeleton texture"],
		["1.2", "6/15", "removed repetitive/unchanged files and compressed others to reduce overall filesize of both packs (22mb -> 5mb)"],
		["1.1", "2/15", "updated guis for both packs; also added a link to here in the pack description"],
	],
	'2019': [
		["1.0.1", "10/14", "changed icons and descriptions of both packs to better reflect my brand at the time"],
		["1.0.0", "10/8", "created this page and therefore officially released the pack to the public"],	
	],
	'Pre-2018': [
		[None, "late 2018", "renamed the pvp overlay \"eli\'s epic gamer pack\" and totally phased out the use of the meme pack"],
		[None, "late 2017", "split the practical aspects of the meme pack into an overlay pack that i used for pvp"],
		[None, "early 2017", "created \"elijah\'s meme pack\", a resource pack mostly made up of inside jokes with few practical assets"],
	]
}

@app.route('/pack')
def pack(): 
	return flask.render_template('pack.html', mcpk = mcpk(), a = a)

@app.route('/pack/changelog')
def pack_changelog(): 
	html = "<style>*{color:#fff;font-family:monospace} p{text-align:justify;line-height:1.25;} h3{text-align:center;}</style>"
	for year in changelog:
		html += f"</p><h3>{year}</h3><p>"
		for version in changelog[year]:
			x = ['v'+version[0],version[1]+'/'+year] if version[0] != None else [version[1],'']
			html += f"<b>{x[0]}</b> - {x[1]} {version[2]}<br><br>"
	return html
