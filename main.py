import flask, waitress, os, re, json
from markupsafe import Markup

app = flask.Flask(__name__) 
app.secret_key = os.environ['sessionkey']

def convert_plaintext(content:str):
	content = flask.make_response(content, 200)
	content.mimetype = 'text/plain'
	return content

class a():

	img = '/static/media/'
	css = '/static/style.css'
	js = '/static/scripts.js'
	logo = '/static/logo.png'
	logo64 = '/static/logo64.png'
	logo128 = '/static/logo128.png'

	twitter = 'https://twitter.com/elisttm'
	youtube = 'https://www.youtube.com/c/elisttm'
	steam = 'https://steamcommunity.com/id/elisttm'
	github = 'https://github.com/elisttm'
	paypal = 'https://paypal.me/thetrashman'

	header_items = (
		('/','home'),
		('/eli','fursona'),
		('/minecraft','minecraft'),
		('/trashbot','trashbot'),
	)

	def md(text, urls=False):
		if urls:
			for x in re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text):
				text = text.replace(x, f'<a href="{x}">{x}</a>')
		for x in re.findall(r'\[(img|video|audio|iframe):(.*?)\]', text):
			if x[0] == 'video' or x[0] == 'audio':
				replacement = f'<{x[0]} controls><source src="{x[1]}" type="{(x[1].rsplit(".", 1))[1]}"></{x[0]}>'
			elif x[0] == 'img':
				replacement = f'<img src="{x[1]}"/>'
			elif x[0] == 'iframe':
				replacement = f'<iframe src="{x[1]}" frameborder="0"></iframe>'
			text = text.replace(f'[{x[0]}:{x[1]}]', replacement)
		for x in re.findall(r'\[(a|c|style):(.*?):(.*?)\]', text):
			if x[0] == 'a':
				replacement = f'<a href="{x[1]}">{x[2]}</a>'
			elif x[0] == 'c':
				replacement = f'<span style="color:{x[1]}">{x[2]}</span>'
			elif x[0] == 'style':
				replacement = f'<span style="{x[1]}">{x[2]}</span>'
			text = text.replace(f'[{x[0]}:{x[1]}:{x[2]}]', replacement)
		for x in re.findall(r'\[(h2|h3|b|i|u|s|sup|sub):(.*?)\]', text):
			text = text.replace(f'[{x[0]}:{x[1]}]', f'<{x[0]}>{x[1]}</{x[0]}>')
		for x in re.findall(r'\[(br|h1)\]', text):
			text = text.replace(f'[{x[0]}]', f'<{x[0]}>')
		return Markup(text)

	sitemap_timeformat = '%Y-%m-%d'
	sitemap_stuff = (
		#url, priority, lastmod (YYYY-MM-DD)
		['', 1.0],
		['eli', 0.9, ''],
		['eli/art', 0.7, ''],
		['trashbot', 0.9],
		['minecraft', 0.9],
		['pack', 0.8],
		['cats', 0.6],
		['gmod', 0.6],
	)

sitemap_pages = ''
for page in a.sitemap_stuff:
	lastmod = f'		<lastmod>{page[2]}</lastmod>\n' if len(page) >= 3 else ''
	sitemap_pages += f"""	<url>\n		<loc>https://elisttm.space/{page[0]}</loc>\n		<priority>{page[1]}</priority>\n		<changefreq>daily</changefreq>\n{lastmod}</url>\n"""
sitemap = f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">\n{sitemap_pages}</urlset>'

@app.route('/sitemap.xml')
def sitemap_xml(): 
	return flask.Response(sitemap, mimetype='text/xml')

@app.route('/robots.txt')
def static_from_root(): 
	return flask.send_from_directory(app.static_folder, flask.request.path[1:])

if __name__ == '__main__':
	import routes
	waitress.serve(app, host='0.0.0.0', port=8080)		# waitress (production)
	#app.run(host="0.0.0.0", port="8080")		# flask (development)