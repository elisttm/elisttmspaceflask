import flask
import waitress
import os
import json
import urllib, urllib.request
import re
from datetime import datetime
from flask import Flask, render_template, send_from_directory, request, redirect, make_response, Markup
from waitress import serve
from data.constants import constants

# 		========================

app = Flask(__name__, 
	static_folder='static', 
	template_folder="templates"
) 

a = constants()

def convert_plaintext(content:str):
	content = make_response(content, 200)
	content.mimetype = "text/plain"
	return content

r_re = r'\[{}(.*?)\]'
replacements_0 = ['br','hr','h1','h2','h3','h4','h5','h6','b','i','u','s','sup','sub']
replacements_1 = {
	'c:': '<span style="color:{}">{}</span>',
	'f:': '<span style="font-family:{}">{}</span>',
	'a:': '<a href="{}">{}</a>',
}

def cformat(c):
	for img_params in re.findall(r_re.format('img:'), c):
		params = img_params.split(":", 1)
		img_class = ''
		if len(params) == 2: 
			img_class = params[1]
		c = c.replace(f'[img:{img_params}]', f'<img src="{params[0]}" class="{img_class}"/>')
	for embed_url in re.findall(r_re.format('embed:'), c):
		if embed_url[-3:].lower() == 'wav' or embed_url[-3:].lower() == 'mp4':
			av_format = 'video'
			if embed_url[-3:].lower() == 'wav':
				av_format = 'audio'
			av_type = av_format+"/"+embed_url[-3:].lower()
			embed_replacement = f'<{av_format} controls><source src="{embed_url}" type="{av_type}"></{av_format}>'
		else:
			embed_replacement = f'<div class="iframe-c"><iframe src="{embed_url}" frameborder="0"></iframe></div>'
		c = c.replace(f'[embed:{embed_url}]', embed_replacement)
	for x, y in replacements_1.items():
		for x_params in re.findall(r_re.format(x), c):
			params = x_params.split(":", 1)
			c = c.replace(f'[{x}{x_params}]', y.format(params[0], params[1]))
	for x in replacements_0:
		for y in re.findall(r_re.format(x), c):
			if y[0] == ':': 
				c = c.replace(f'[{x}{y}]', f'<{x}>{y[1:]}</{x}>')
			else: 
				c = c.replace(f'[{x}]', f'<{x}>')
	return Markup(c)

# 		========================

# special case routes for root files

@app.route('/robots.txt')
@app.route('/sitemap.xml')
@app.route('/favicon.ico')
def static_from_root():
	return send_from_directory(app.static_folder, request.path[1:])

# 		========================

if __name__ == '__main__':
	import routes
	serve(app, host='0.0.0.0', port=8080)		# waitress (production)
#	app.run(host="0.0.0.0", port="8080")		# flask (development)